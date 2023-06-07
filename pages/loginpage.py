from locators import LoginPageLocators
from .basepage import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def set_username_and_password(self, username, password):
        username_field = self.element_is_visible(locator=self.locators.INPUT_USERNAME)
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.element_is_visible(locator=self.locators.INPUT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        submit_button = self.element_is_clickable(self.locators.BUTTON_SUBMIT)
        submit_button.click()

    def get_error_message(self):
        return self.element_is_visible(locator=self.locators.ERROR_MESSAGE).text

    def get_wrong_email_field(self):
        return self.element_is_visible(locator=self.locators.EMAIL_ERROR).text

    def logout(self):
        self.element_is_visible(locator=self.locators.LOGOUT_LINK).click()
