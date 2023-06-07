from selenium.webdriver.common.by import By


class AddNewCustomerLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#LastName')
    GENDER_MALE_FIELD = (By.CSS_SELECTOR, f'#Gender_Male')
    GENDER_FEMALE_FIELD = (By.CSS_SELECTOR, '#Gender_Female')
    DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, '#DateOfBirth')
    COMPANY_NAME_FIELD = (By.CSS_SELECTOR, '#Company')
    IS_TAX_EMPT_FIELD = (By.CSS_SELECTOR, '#IsTaxExempt')
    NEWSLETTER_FIELD = (By.CSS_SELECTOR, '#SelectedNewsletterSubscriptionStoreIds_listbox')
    CUSTOMER_ROLES = (By.CSS_SELECTOR, '#SelectedCustomerRoleIds-list')
    CUSTOMER_ROLE_SELECT_FIELD = (By.CSS_SELECTOR, '[name="SelectedCustomerRoleIds"]')
    REGISTERED_DELETE_ROLE = (By.CSS_SELECTOR, 'ul#SelectedCustomerRoleIds_taglist span[title="delete"]')
    MANAGER_OF_VENDOR_FIELD = (By.CSS_SELECTOR, '#VendorId')
    ADMIN_COMMENT_FIELD = (By.CSS_SELECTOR, '#AdminComment')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[name="save"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    SUCCESS_MESSAGE_FIELD = (By.CSS_SELECTOR, 'div.alert-success>button.close')
