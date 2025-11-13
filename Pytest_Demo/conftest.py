
import pytest
import os
from selenium import webdriver

@pytest.fixture(scope="session")
def base_url():
    print("Inside base_url")
    #Get Base URL from environment variable
    return os.getenv("BASE_URL","https://facebook.com")
@pytest.fixture(scope="function")
def driver():
    print("Inside driver")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()