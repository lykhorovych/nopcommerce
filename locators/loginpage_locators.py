from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, '#Email')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#Password')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '.login-button')
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href$='/logout']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.message-error')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#Email-error')
