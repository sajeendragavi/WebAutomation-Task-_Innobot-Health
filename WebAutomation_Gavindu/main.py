from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from database.db_connector import insert_product

driver = webdriver.Chrome()

try:
    home_page = HomePage(driver)
    home_page.search("Mobile Phones")

    results_page = SearchResultsPage(driver)
    products = results_page.get_product_details()

    for product in products:
        print(f"Inserting: {product}")
        insert_product(
            product["name"],
            product["price"],
            product["availability"],
            product["rating"]
        )
finally:
    driver.quit()
