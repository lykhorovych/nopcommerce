from locators import SearchPageLocators
from .basepage import BasePage


class SearchPage(BasePage):
    locators = SearchPageLocators()

    def set_email_field(self, email):
        email_field = self.element_is_visible(locator=self.locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    def set_first_name(self, firstname):
        first_name_field = self.element_is_present(locator=self.locators.FIRST_NAME_FIELD)
        first_name_field.clear()
        first_name_field.send_keys(firstname)

    def set_last_name(self, lastname):
        last_name_field = self.element_is_present(locator=self.locators.LAST_NAME_FIELD)
        last_name_field.clear()
        last_name_field.send_keys(lastname)

    def click_button_search(self):
        self.element_is_present(locator=self.locators.SEARCH_BUTTON).click()

    def find_NOR_table(self):
        result_element = self.element_is_present(locator=self.locators.RESULT_TABLE_ELEMENT_BY_EMAIL)
        return result_element

    def check_out_result(self):
        table = self.element_is_present(locator=self.locators.RESULT_TABLE_ELEMENT_BY_NAME)
        return table
