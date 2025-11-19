
import pytest
import os
from selenium import webdriver
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def base_url():
    print("Inside base_url")
    #Get Base URL from environment variable
    return os.getenv("BASE_URL","https://saucedemo.com")

@pytest.fixture(scope="function")
def driver():
    logging.info("Starting Chrome driver")
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # Optional: Disable leak detection if desired
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    logging.info("Quitting Chrome driver")
    driver.quit()

@pytest.fixture(scope="function")
def login(request, driver, base_url ):
    """
    Log in before each test function.
    Uses parametrize values from the test.
    """
    username = request.param["username"]
    password = request.param["password"]


    driver.get(base_url)

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "login-button").click()


    # Verify inventory page loaded
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    print(f"Login successful for user: {username}")

    return driver,request.param