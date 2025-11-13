from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import Logger
import time

driver = webdriver.Chrome()
print(driver.capabilities['browserVersion'])
driver.get("https://facebook.com")
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//input[@id='email']"))
)

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("samp")
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("pass")
driver.find_element(By.CSS_SELECTOR,"button[name='login']").click()
time.sleep(10)
#driver.implicitly_wait(10)
driver.quit()
Logger.info("passed")

