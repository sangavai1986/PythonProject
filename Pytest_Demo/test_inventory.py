import logging
import time

import pytest
from selenium.webdriver.common.by import By

inventory_data = [
    {"username": "standard_user", "password": "secret_sauce","products": ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
 },
]

@pytest.mark.parametrize("login", inventory_data, indirect=True)
def test_add_products_to_cart(login,request):

    driver,params = login
    driver.get("https://www.saucedemo.com/inventory.html")
    username = params["username"]
    products = params["products"]
    product_count = len(products)
    #products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    for product_name in products:

        add_button = driver.find_element(By.XPATH, f"//div[text()='{product_name}']/following::button[1]")
        add_button.click()
        remove_button = driver.find_element(By.XPATH, f"//div[text()='{product_name}']/following::button[1]")
        if remove_button.text == "Remove":
            print(f"product {product_name} added to cart\n")
        #print(f"product {product_name} added to cart\n")
    # Verify shopping cart badge
    try:
        badge = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']").text
        #print("PRODUCTS "+products)
        print("PRODUCT COUNT "+badge)
        #print("LENGTH "+len(products))
        assert int(badge) == product_count
        logging.info(f"{len(products)} products added to cart for {username}")
    except:
        logging.error(f"Cart badge not found for {username}")

    # Navigate to cart page
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()