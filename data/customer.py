import json
from dataclasses import dataclass
from random import choice

from faker import Faker

faker_eng = Faker()
faker_eng.random.seed(4321)


@dataclass
class Customer:
    firstname: str
    lastname: str
    email: str
    password: str
    gender: str
    company_name: str
    manager_of_vendor: str
    date_of_birth: str
    customer_roles: str
    admin_comment: str

    def __init__(self, firstname=None, lastname=None, email=None, password=None,
                 gender=None, company_name=None, manager_of_vendor=None, date_of_birth=None,
                 customer_roles=None, admin_comment=None):
        self.firstname = faker_eng.unique.first_name() if firstname is None else firstname
        self.lastname = faker_eng.unique.last_name() if lastname is None else lastname
        self.email = faker_eng.unique.email() if email is None else email
        self.password = faker_eng.unique.password() if password is None else password
        self.gender = choice(['Male', 'Female']) if gender is None else gender
        self.company_name = faker_eng.unique.company() if company_name is None else company_name
        self.manager_of_vendor = choice(['Vendor 1', 'Vendor 2']) if manager_of_vendor is None else manager_of_vendor
        self.date_of_birth = f"{faker_eng.month()}/{faker_eng.day_of_month()}/{faker_eng.year()}" if date_of_birth is None else date_of_birth
        self.customer_roles = choice(['Registered', 'Vendors', 'Guests', 'Forum Moderators',
                                      'Administrators']) if customer_roles is None else customer_roles
        self.admin_comment = faker_eng.unique.text() if admin_comment is None else admin_comment

    @classmethod
    def create_customer(cls, **kwargs: dict):
        return cls(**kwargs)

    def to_dict(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'password': self.password,
            'gender': self.gender,
            'company_name': self.company_name,
            'manager_of_vendor': self.manager_of_vendor,
            'date_of_birth': self.date_of_birth,
            'customer_roles': self.customer_roles,
            'admin_comment': self.admin_comment
        }


for _ in range(3):
    customer = Customer()
    print(customer.to_dict())


def generate_customers():
    customers = [Customer().to_dict() for _ in range(10)]
    with open('./customers.json', 'w') as file:
        json.dump(customers, file, indent=8)


def read_data():
    generate_customers()
    with open('./customers.json') as file:
        data = json.load(file)
        return data


if __name__ == '__main__':
    generate_customers()
