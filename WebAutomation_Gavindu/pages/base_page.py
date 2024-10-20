from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=12):
        """Wait for an element to be visible."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Click an element."""
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Enter text into an input field."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
