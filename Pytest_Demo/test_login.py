import time

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from seleniumbase.common.exceptions import TimeoutException


@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)


def testlogin(demo_fixture):
    logging.info("Login successful")


#@pytest.mark.parametrize("driver", ["chrome", "firefox", "edge"], indirect=True)
@pytest.mark.parametrize(
    "login",
    [
        {"username": "standard_user", "password": "secret_sauce"},
        {"username": "visual_user", "password": "secret_sauce"},
    ],
    indirect=True  # tells pytest to pass these dicts to the fixture
)
def test_login_with_users(login):
    (driver,username) = login
    # Verify inventory page logo
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"
    logging.info(f"Login passed for {username}")


# @pytest.mark.regression
# def testlogoff():
#     print("Logoff success")
#
# @pytest.mark.skip
# def testcalc():
#     assert 2+2 ==4
#
# @pytest.mark.xfail
# def testcalc1():
#     assert 3+2 == 4