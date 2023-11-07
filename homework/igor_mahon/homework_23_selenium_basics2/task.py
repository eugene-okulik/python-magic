"""
Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form
и полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
После отправки вам будет отображено окошко с тем что вы ввели.
Получите со страницы содержимое этого окошка и распечатайте (выведите на экран).
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the window
driver.maximize_window()

# Go to https://demoqa.com/automation-practice-form
driver.get('https://demoqa.com/automation-practice-form')

# Locate and input first name
driver.find_element(By.ID, 'firstName').send_keys('Glenn')

# Locate and input last name
driver.find_element(By.ID, 'lastName').send_keys('Miller')

# Locate and input email
driver.find_element(By.ID, 'userEmail').send_keys('glen@miller.com')

# Locate and click the "male" radio button
driver.find_element(By.XPATH, "//div[@id='genterWrapper']/div[2]/div[1]/label").click()

# Locate and input Mobile
driver.find_element(By.CSS_SELECTOR, '[placeholder = "Mobile Number"]').send_keys('3231231231')

# Create ActionChains object
actions = ActionChains(driver)

# Locate and input Subject
input_subject = driver.find_element(By.XPATH, "//div[@id='subjectsWrapper']/div[2]/div[1]/div[1]/div[1]")
actions.click(input_subject).send_keys('NEW SUBJECT!').perform()

# Locate calendar and click calendar
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.CLASS_NAME, 'react-datepicker__day--today').click()

# Locate and select a hobby
driver.find_element(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[1]").click()

# Locate and input Current Address
driver.find_element(By.CSS_SELECTOR, '[placeholder = "Current Address"]').send_keys('Vitebsk')

# Locate and select State
state_picklist = driver.find_element(By.XPATH, '//div[@id="state"]/div/div[2]')
# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView();", state_picklist)
# Perform the click action
actions.click(state_picklist).send_keys(Keys.ENTER).perform()

# Locate and select City
city_picklist = driver.find_element(By.XPATH, '//div[@id="city"]/div/div[2]')
# Perform the click action
actions.click(city_picklist).send_keys(Keys.ENTER).perform()

# Locate and click Submit using JavaScript - I don't find another way to click this button
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
driver.execute_script("arguments[0].click();", submit_button)

# Locate and print information from Modal
wait = WebDriverWait(driver, 10)
modal_window = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
# Print information from the Modal
print(modal_window.text)  # .text is used to extract the text content from a WebElement in Selenium
