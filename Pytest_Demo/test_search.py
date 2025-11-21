import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


search_users = [
    {"username": "standard_user", "password": "secret_sauce", "products": ["Sauce Labs Backpack"]},
   ]

@pytest.mark.parametrize("login", search_users, indirect=True)
def test_search_product(login, request):
    (driver, params) = login
    print(params["username"])
    print(params["products"])
    driver.get("https://www.saucedemo.com/inventory.html")
    #print(f"Perform search actions for {search_users['username']}")
    # Example search: find product by name
    product_count = len(params["products"])
    for product in params["products"]:
        print("PRODUCT NAME: "+product)
        product_name = "Sauce Labs Backpack"
        try:
            element = driver.find_element(By.XPATH, f"//div[text()='{product_name}']")
            assert element.is_displayed()
            logging.info(f"Product '{product_name}' found")
        except:
            logging.error(f"Product '{product_name}' not found")


