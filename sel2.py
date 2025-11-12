from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id ="bigCookie"
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH,"//*[contains(text(), 'English')]")
language.click()
cookie = driver.find_element(By.ID,cookie_id)
#cookie.click()
increment = 6
while increment:
    cookie.click()
    cookies_count = driver.find_element(By.ID,"cookies").text.split(" ")[0]
    print(cookies_count)
    increment = increment - 1

time.sleep(5)