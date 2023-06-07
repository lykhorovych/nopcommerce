import time

import pytest

from pages import LoginPage
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestLoginPageCase:
    LOGIN_URL = ReadConfig.geturl()
    USER_NAME = ReadConfig.getusername()
    PASSWORD = ReadConfig.getpassword()

    logger = LogGen.get_logger()

    logger.info("*" * 5 + 'Test_01_Login' + "*" * 5)

    def test_title_login_page(self, driver):
        self.logger.info("*" * 5 + 'Start automation test Login Page' + "*" * 5)
        login_page = LoginPage(driver, url=self.LOGIN_URL)
        login_page.open()
        time.sleep(10)
        expected_title = 'Your store. Login'
        title = login_page.driver.title
        if title == expected_title:
            self.logger.info("*" * 5 + "Test title Login Page is passed" + "*" * 5)
        else:
            login_page.driver.save_screenshot('.\\screenshots\\testTitleLogin.png')
            self.logger.error("*" * 5 + "TEST title Login Page is failed" + "*" * 5)
            self.logger.error(msg=f'{title} != {expected_title}')
        self.logger.info("*" * 5 + 'End automation test Login Page' + "*" * 5)
        assert title == expected_title

    @pytest.mark.parametrize("login, password, error_message", [('admin@yourstore.com', '1234',
                                                                 "Login was unsuccessful. Please correct the errors and try again.\nThe credentials provided are incorrect"),
                                                                ('admin1@yourstore.com', 'admin',
                                                                 "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
                                                                 )])
    def test_login_to_admin_page_failed(self, driver, login, password, error_message):
        self.logger.info(msg="Start Test login to admin failed")
        login_page = LoginPage(driver, url=self.LOGIN_URL)
        login_page.open()
        time.sleep(10)
        login_page.set_username_and_password(username=login, password=password)
        if error_message != login_page.get_error_message():
            login_page.driver.save_screenshot('../screenshots/TestLoginFailed.png')
            self.logger.error(msg="Test login to admin page is failed")
        else:
            self.logger.info(msg="Test login to admin page is passed")
        self.logger.info("Test End login admin failed")
        assert error_message == login_page.get_error_message()

    def test_login_to_admin_page_wrong_email_form(self, driver):
        self.logger.info(msg="Start Test login to admin failed")
        login_page = LoginPage(driver, url=self.LOGIN_URL)
        login_page.open()
        time.sleep(10)
        error_message = 'Wrong email'
        login_page.set_username_and_password(username='admin', password='admin')
        if error_message != login_page.get_wrong_email_field():
            login_page.driver.save_screenshot('../screenshots/TestLoginWrongEmailFailed.png')
            self.logger.error(msg="Test login to admin page is failed")
        else:
            self.logger.info(msg="Test login to admin page is passed")
        self.logger.info("Test End login admin failed")
        assert error_message == login_page.get_wrong_email_field()

    def test_login_to_admin_page_positive(self, driver):
        login_page = LoginPage(driver, url=self.LOGIN_URL)
        login_page.open()
        time.sleep(10)
        self.logger.info("*" * 5 + 'Start automation test Admin Page' + "*" * 5)
        login_page.set_username_and_password(username=self.USER_NAME, password=self.PASSWORD)
        expected_title = 'Dashboard / nopCommerce administration'
        current_title = login_page.driver.title
        if current_title == expected_title:
            self.logger.info("*" * 5 + "Test title Admin Page is passed" + "*" * 5)
        else:
            login_page.driver.save_screenshot('.\\screenshots\\testLoginAdminPage.png')
            text = f'{current_title} != {expected_title}'
            self.logger.error("*" * 5 + "Test title Admin Page is failed" + "*" * 5)
            self.logger.error(msg=text)
        self.logger.info("*" * 5 + 'End automation test Admin Page' + "*" * 5)
        assert current_title == expected_title
