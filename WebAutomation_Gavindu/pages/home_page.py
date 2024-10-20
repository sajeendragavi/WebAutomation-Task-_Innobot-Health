from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, "query")  # Locator for Ikman.lk search box
    SEARCH_BUTTON = (By.CLASS_NAME, "btn--1gFez")  # Locator for the search button

    def __init__(self, driver):
        """Initialize the HomePage and load Ikman.lk."""
        super().__init__(driver)
        self.driver.get("https://ikman.lk/")

    def search(self, text):
        """Perform a search for the given text."""
        # Wait until the backdrop becomes invisible
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "portal-backdrop--2zF8l"))
        )

        # Wait for the search box to be present and enter text
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SEARCH_BOX)
        )
        self.enter_text(self.SEARCH_BOX, text)  # Make sure this method exists in BasePage

        # Ensure the search button is clickable and then click it
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        try:
            time.sleep(1)
            search_button.click()
        except Exception as e:
            print(f"Error clicking the search button: {e}")
            # Fallback to JavaScript click if normal click fails
            self.driver.execute_script("arguments[0].click();", search_button)
