from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

import logging
import Logger
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')


driver = webdriver.Chrome();
print(driver.capabilities['browserVersion'])
driver.get("https://facebook.com")
#driver.implicitly_wait(10)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//input[@id='email']"))
)


#input_element = driver.find_element(By.XPATH,"//input[@id='email']")
#input_element.clear()
#input_element.send_keys("Python" +Keys.ENTER)
'''
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Python Tutorial"))
)

'''
driver.implicitly_wait(10)
#page = driver.page_source;
#print(page);
#soup = BeautifulSoup(page,'html.parser');
#print(soup.prettify());

links = driver.find_elements(By.TAG_NAME,"a");
print("Title : "+driver.title);
for link in links:
    print(link.get_attribute("href"))

#link = driver.find_element(By.PARTIAL_LINK_TEXT,"Python Tutorial")

#link.click()

#time.sleep(10)

driver.quit()
Logger.info("passed")
