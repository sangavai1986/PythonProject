from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get("https://demoqa.com/radio-button")  # Replace with your target URL

# Wait for page to load (adjust time or use WebDriverWait for more reliability)
time.sleep(2)


yes_label = driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
driver.execute_script("arguments[0].scrollIntoView(true);", yes_label)

# Click the label (which will select the radio button)
yes_label.click()
yes_label = driver.find_element(By.ID,"yesRadio")
time.sleep(5)
if yes_label.is_selected():
    print("Radio is selected")
else:
    print("Radio button Yes not selected")

driver.quit()