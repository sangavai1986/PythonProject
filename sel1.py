from selenium import webdriver
import chromedriver_autoinstaller
#from selenium.webdriver.chrome.options import Options
def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options

options = get_default_chrome_options()
driver = webdriver.Chrome(options=options)

#chromedriver_autoinstaller.install()
#driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#driver.implicitly_wait(4)
print(driver.capabilities['browserVersion'])
driver.quit()
