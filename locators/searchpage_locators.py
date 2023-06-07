from selenium.webdriver.common.by import By


class SearchPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="SearchEmail"]')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="SearchFirstName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="SearchLastName"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button#search-customers')
    RESULT_TABLE_ELEMENT_BY_EMAIL = (By.XPATH, '//table[@id="customers-grid"]/tbody/tr[1]/td[2]')
    RESULT_TABLE_ELEMENT_BY_NAME = (By.XPATH, '//table[@id="customers-grid"]/tbody/tr[1]/td[3]')
