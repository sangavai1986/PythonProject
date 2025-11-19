import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def loginpage():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.ID,"user-name"))
    )
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    time.sleep(10)
    driver.find_element(By.NAME,"login-button").click()
    time.sleep(10)
    logo = driver.find_element(By.XPATH,"//div[text()='Swag Labs']")
    if logo.text == 'Swag Labs':
        print("Entered the inventory page")

    driver.quit()

loginpage()