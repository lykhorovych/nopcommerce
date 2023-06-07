from selenium.webdriver.common.by import By


class AdminPageLocators:
    CUSTOMERS_MENU_LINK = (By.XPATH, '//a[@href="#"]//p[contains(text(), "Customers")]')
    CUSTOMERS_MENU_ITEM_LINK = (By.CSS_SELECTOR, 'li.nav-item a[href*="Admin/Customer/List"]')
    ADD_NEW_CUSTOMER_LINK = (By.CSS_SELECTOR, 'a[href*="Customer/Create"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='SearchEmail']")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='SearchFirstName']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='SearchLastName']")
