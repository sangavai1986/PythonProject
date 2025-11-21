import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pytest_Demo.conftest_old import logout

'''
driver = webdriver.Chrome()
driver.get("https://saucedemo.com")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(10)
driver.find_element(By.NAME, "login-button").click()
time.sleep(10)
driver.quit()
'''
@pytest.mark.parametrize(
    "login",
    [
        {"username": "standard_user", "password": "secret_sauce"},

    ],
    indirect=True
)

def test_logoff(login):
    driver,params = login

    logout(driver)
    print(driver.title)
    try:
        assert "Swag" in driver.title
        logging.info(f"User {params['username']} logged off")
    except BaseException as e:
        logging.info(f"User {params['username']} Log off unsuccessful")
        logging.info("ERROR IS"+e)
