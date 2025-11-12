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
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(options=options)
#print(driver.capabilities['browserVersion'])
#service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome();
print(driver.capabilities['browserVersion'])
driver.get("https://www.google.com")
#driver.implicitly_wait(10)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID,"APjFqb"))
)

input_element = driver.find_element(By.ID,"APjFqb")
#input_element.clear()
input_element.send_keys("Python" +Keys.ENTER)
'''
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Python Tutorial"))
)

'''
driver.implicitly_wait(10);
#page = driver.page_source;
#print(page);
#soup = BeautifulSoup(page,'html.parser');
#print(soup.prettify());
results = driver.find_elements(By.CSS_SELECTOR,"h3");
for result in results:
    title = result.text;
    link = driver.find_element(By.XPATH,"..").get_attribute("href");
    print("Title : "+title);
    print("Link :"+link);
#link = driver.find_element(By.PARTIAL_LINK_TEXT,"Python Tutorial")

#link.click()

#time.sleep(10)

driver.quit()
Logger.info("passed")

''' 
Hello
'''

