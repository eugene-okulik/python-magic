"""
Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form
и полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
После отправки вам будет отображено окошко с тем что вы ввели.
Получите со страницы содержимое этого окошка и распечатайте (выведите на экран).
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Locate and input Subject
driver.find_element(By.ID, "subjectsInput").send_keys("a new subject")

# Locate calendar and click calendar
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.CLASS_NAME, 'react-datepicker__day--today').click()

# Locate and select a hobby
driver.find_element(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[1]/label")

# Locate and input Current Address
driver.find_element(By.CSS_SELECTOR, '[placeholder = "Current Address"]').send_keys('Vitebsk')

# Set the zoom level to 50% to see picklists State and City
driver.execute_script("document.body.style.zoom = '50%'")

# Locate and click Submit
element = driver.find_element(By.ID, 'submit')
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
# Locate and select State
# driver.find_element(By.CLASS_NAME, 'css-1uccc91-singleValue').click()

sleep(2)
