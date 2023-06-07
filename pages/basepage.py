from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_present(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshots()
            return False

    def elements_are_present(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshots()
            return False

    def element_is_visible(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
            return element
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshots()
            return False

    def elements_are_visible(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
            return element
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshots()
            return False

    def element_is_clickable(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))
            return element
        except (NoSuchElementException, TimeoutException):
            return False
