from pages import LoginPage, AdminPage, SearchPage
from utilities.customlogger import LogGen


class TestAdminPage:
    LOGIN_URL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"  # ReadConfig.geturl()
    USER_NAME = "admin@yourstore.com"  # ReadConfig.getusername()
    PASSWORD = "admin"  # ReadConfig.getpassword()

    logger = LogGen.get_logger()

    # @pytest.mark.parametrize("customer", [Customer() for _ in range(10)])
    def test_add_new_customer(self, ud_driver, customer):
        login_page = LoginPage(driver=ud_driver, url=self.LOGIN_URL)
        login_page.open()
        self.logger.info("Start login")
        login_page.set_username_and_password(self.USER_NAME, self.PASSWORD)
        addnc_page = AdminPage(driver=ud_driver)
        addnc_page.find_and_click_on_customers_menu_link()
        addnc_page.find_and_click_on_customers_menu_item_link()
        addnc_page.find_and_click_add_new_customer()
        addnc_page.add_email_and_password(email=customer.email, password=customer.password)
        addnc_page.add_first_and_lastname(firstname=customer.firstname, lastname=customer.lastname)
        addnc_page.add_company_name(name=customer.company_name)
        addnc_page.set_gender(gender=customer.gender)
        addnc_page.add_admin_content(content=customer.admin_comment)
        addnc_page.add_date_of_birth(date=customer.date_of_birth)
        addnc_page.add_vendor_role(role=customer.manager_of_vendor)
        addnc_page.add_customer_roles()
        # addnc_page.set_newsletter()
        addnc_page.click_save()
        expected_success_message = "×\nThe new customer has been added successfully."
        success_message = addnc_page.get_success_message()
        if success_message:
            assert expected_success_message == success_message.text
            self.logger.info('New customer is successfully created')
            self.logger.info("The test passed")
        else:
            self.logger.error('Test is failed')
            addnc_page.driver.save_screenshot('.\\screenshots\\testAddNewCustomer.png')

    def test_search_customer_by_email(self, ud_driver):
        login_page = LoginPage(ud_driver, url=self.LOGIN_URL)
        login_page.open()
        login_page.set_username_and_password(username=self.USER_NAME, password=self.PASSWORD)
        self.logger.info("Start login")
        admin_page = AdminPage(ud_driver)
        admin_page.find_and_click_on_customers_menu_link()
        admin_page.find_and_click_on_customers_menu_item_link()

        search_page = SearchPage(ud_driver)
        search_page.set_email_field(email='kiyjcycyhjc676008@gmail.com')
        search_page.click_button_search()
        if search_page.find_NOR_table():
            result = search_page.find_NOR_table().text
            expected_email = 'kiyjcycyhjc676008@gmail.com'
            assert result == expected_email
            print('Test is passed')
            self.logger.info('Test is passed')
        else:
            assert True == False
            print('Test is failed')
            self.logger.error('Test is failed')
            search_page.driver.save_screenshot('.\\screenshots\\testSearchByEmail.png')

    def test_search_customer_by_name(self, ud_driver):
        login_page = LoginPage(ud_driver, url=self.LOGIN_URL)
        login_page.open()
        login_page.set_username_and_password(username=self.USER_NAME, password=self.PASSWORD)
        self.logger.info("Start login")
        admin_page = AdminPage(ud_driver)
        admin_page.find_and_click_on_customers_menu_link()
        admin_page.find_and_click_on_customers_menu_item_link()

        search_page = SearchPage(ud_driver)
        search_page.set_first_name(firstname="Virat")
        search_page.set_last_name(lastname="Kohli")
        search_page.click_button_search()
        if search_page.check_out_result():
            result = search_page.check_out_result().text
            expected_name = 'Virat Kohli'
            assert result == expected_name
            print('Test is passed')
            self.logger.info('Test is passed')
        else:
            assert True == False
            print('Test is failed')
            self.logger.error('Test is failed')
            search_page.driver.save_screenshot('.\\screenshots\\testSearchByName.png')
