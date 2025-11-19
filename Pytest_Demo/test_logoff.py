import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
user_data = [ {"username": "standard_user","password": "secret_sauce"}]
@pytest.mark.parametrize( "login",user_data ,indirect=True)
def test_logoff(login,request):
    driver,params = login
    driver.find_element(By.ID,"react-burger-menu-btn").click()
    driver.find_element(By.ID,"logout_sidebar_link").click()
    time.sleep(10)
    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH,"//div[text()='Swag Labs']"))
    )