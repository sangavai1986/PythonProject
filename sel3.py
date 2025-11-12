from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from XMLParser.parser import load_user_data
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time

data = load_user_data('testdata.xml')
print(data['email'])

# Set up WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get("https://demoqa.com/automation-practice-form")  # Replace with your target URL

# Wait for page to load (adjust time or use WebDriverWait for more reliability)
time.sleep(2)


# 1. Enter text into a text field
text_field = driver.find_element(By.ID, "firstName")  # Replace with actual text field ID
text_field.clear()
text_field.send_keys(data['first_name'])

text_field = driver.find_element(By.ID, "lastName")  # Replace with actual text field ID
text_field.clear()
text_field.send_keys(data['last_name'])

text_field = driver.find_element(By.ID, "userEmail")  # Replace with actual text field ID
text_field.clear()
text_field.send_keys(data['email'])

time.sleep(3)
# Find the radio button by its value and click it

print(data['gender'])
gender = data['gender']
if(gender == "Male"):
    label = "label[for='gender-radio-1']"
    element_id = 'gender-radio-1'
elif(gender == "Female"):
    label = "label[for='gender-radio-2']"
    element_id ='gender-radio-2'
else:
    label = "label[for='gender-radio-3']"
    element_id = 'gender-radio-3'

radio = driver.find_element(By.CSS_SELECTOR, label)
driver.execute_script("arguments[0].scrollIntoView(true);", radio)
radio.click()

element = driver.find_element(By.ID, element_id)

if element.is_selected():
    print(f"{gender} gender is selected ✅")
else:
    print(f"{gender}' gender is NOT selected ❌")
# Confirm the radio button is selected
'''
checked = driver.execute_script("return document.getElementById('element').checked;")
print("Checked state via JS:", checked)
#female_label = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']")
#driver.execute_script("arguments[0].scrollIntoView(true);", female_label)
if checked:
    print("Radio button "+gender+" is selected ✅")
else:
    print("Radio button "+gender+" is NOT selected ❌")
'''
text_field = driver.find_element(By.ID, "userNumber")  # Replace with actual text field ID
text_field.clear()
text_field.send_keys(data['mobile'])

'''text_field = driver.find_element(By.ID, "dateOfBirthInput")  # Replace with actual text field ID
text_field.clear()
text_field.send_keys("11111987")'''

# 2. Select a value from dropdown
wait = WebDriverWait(driver, 10)
input_box = wait.until(EC.presence_of_element_located((By.ID, "subjectsInput")))

# Type the subject (e.g., 'Math')
input_box.send_keys(data['subject'])

# Wait for suggestions to appear
time.sleep(1)  # You can use WebDriverWait + visibility_of_element_located if needed

# Press ENTER to select the first suggestion
input_box.send_keys(Keys.ENTER)

#3. Find checkbox by ID
'''
checkbox = driver.find_element(By.ID, "hobbies-checkbox-1")

# If not selected, click it
if not checkbox.is_selected():
    checkbox.click()

# Confirm if it's selected
if checkbox.is_selected():
    print("Checkbox is selected ✅")
else:
    print("Checkbox is NOT selected ❌")
'''
wait = WebDriverWait(driver, 10)

# List of labels to click
hobbies_to_select = ["Sports", "Reading", "Music"]
print(data['hobbies'])
for hobby in data['hobbies']:
    # Find label element with exact text
    label = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        f"//label[text()='{hobby}']"
    )))
    label.click()

    # Optional: verify checkbox is selected
    checkbox_id = label.get_attribute("for")
    checkbox = driver.find_element(By.ID, checkbox_id)
    assert checkbox.is_selected(), f"{hobby} checkbox was NOT selected ❌"
    print(f"{hobby} checkbox is selected ✅")
# Wait and quit
time.sleep(2)




# 4. Click the OK button
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
driver.execute_script("arguments[0].click();", submit_button)
#ok_button = driver.find_element(By.ID, "submit")  # Replace with actual button ID
#ok_button.click()

# Wait for result or confirmation (optional)
time.sleep(3)

# Close the browser
driver.quit()