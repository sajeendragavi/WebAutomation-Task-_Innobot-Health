from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, "title--3yncE")
    PRODUCT_PRICE = (By.CLASS_NAME, "price--3SnqI")
    PRODUCT_AVAILABILITY = (By.CLASS_NAME, "description--2-ez3")  # Adjust locator if needed
    PRODUCT_RATING = (By.CLASS_NAME, "rating--1gkAq")  # If available; modify as needed

    def get_product_details(self):
        """Extracts name, price, availability, and rating of products."""
        products = []

        names = self.driver.find_elements(*self.PRODUCT_NAME)
        prices = self.driver.find_elements(*self.PRODUCT_PRICE)
        availabilities = self.driver.find_elements(*self.PRODUCT_AVAILABILITY)
        ratings = self.driver.find_elements(*self.PRODUCT_RATING)

        for i in range(len(names)):
            product = {
                "name": names[i].text,
                "price": prices[i].text if i < len(prices) else "N/A",
                "availability": availabilities[i].text if i < len(availabilities) else "N/A",
                "rating": ratings[i].text if i < len(ratings) else "N/A"

            }
            products.append(product)

        return products
