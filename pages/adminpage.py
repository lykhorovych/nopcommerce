from selenium.webdriver.support.ui import Select

from locators import AdminPageLocators, AddNewCustomerLocators
from .basepage import BasePage


class AdminPage(BasePage):
    admin_locators = AdminPageLocators()
    add_new_locators = AddNewCustomerLocators()

    def find_and_click_on_customers_menu_link(self):
        self.element_is_present(locator=self.admin_locators.CUSTOMERS_MENU_LINK).click()

    def find_and_click_on_customers_menu_item_link(self):
        self.element_is_present(locator=self.admin_locators.CUSTOMERS_MENU_ITEM_LINK).click()

    def find_and_click_add_new_customer(self):
        self.element_is_present(locator=self.admin_locators.ADD_NEW_CUSTOMER_LINK).click()

    def add_email_and_password(self, email, password):
        email_field = self.element_is_present(locator=self.add_new_locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
        password_field = self.element_is_present(locator=self.add_new_locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def add_first_and_lastname(self, firstname, lastname):
        firstname_field = self.element_is_present(locator=self.add_new_locators.FIRSTNAME_FIELD)
        firstname_field.clear()
        lastname_field = self.element_is_present(locator=self.add_new_locators.LASTNAME_FIELD)
        lastname_field.clear()
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)

    def set_gender(self, gender='Male'):
        if gender == 'Male':
            self.element_is_present(locator=self.add_new_locators.GENDER_MALE_FIELD).click()
        else:
            self.element_is_present(locator=self.add_new_locators.GENDER_FEMALE_FIELD).click()

    def add_company_name(self, name):
        company_name = self.element_is_present(locator=self.add_new_locators.COMPANY_NAME_FIELD)
        company_name.clear()
        company_name.send_keys(name)

    def set_newsletter(self, value='1'):
        select = self.elements_are_present(locator=self.add_new_locators.NEWSLETTER_FIELD)
        self.driver.execute_script("arguments[0].click();", select)

    def add_admin_content(self, content=''):
        el = self.element_is_present(locator=self.add_new_locators.ADMIN_COMMENT_FIELD)
        el.send_keys(content)

    def add_date_of_birth(self, date='09/19/1983'):
        date_field = self.element_is_present(locator=self.add_new_locators.DATE_OF_BIRTH_FIELD)
        date_field.send_keys(date)

    def add_vendor_role(self, role='Vendor 2'):
        vendor_role_field = Select(self.element_is_present(locator=self.add_new_locators.MANAGER_OF_VENDOR_FIELD))
        vendor_role_field.select_by_visible_text(text=role)

    def add_customer_roles(self, role='Guests'):
        # self.element_is_present(locator=self.add_new_locators.CUSTOMER_ROLES)
        self.driver.execute_script("document.getElementById('SelectedCustomerRoleIds').style.display='block';")
        select = Select(self.element_is_present(locator=self.add_new_locators.CUSTOMER_ROLE_SELECT_FIELD))
        selected_values = select.all_selected_options
        if 'Registered' in [option.text for option in selected_values] and role == 'Guests':
            self.element_is_present(locator=self.add_new_locators.REGISTERED_DELETE_ROLE).click()
        select.select_by_visible_text(text=role)

    def click_save(self):
        self.element_is_present(locator=self.add_new_locators.SAVE_BUTTON).click()

    def get_success_message(self):
        return self.element_is_visible(locator=self.add_new_locators.SUCCESS_MESSAGE)
