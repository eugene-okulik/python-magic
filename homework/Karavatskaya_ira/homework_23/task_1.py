from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# указываем путь к драйверу браузера (путь к ChromeDriver)
driver = webdriver.Chrome()
driver.maximize_window()

sleep(3)

# Заходим на страницу
driver.get('https://demoqa.com/automation-practice-form')


# Заполняем форму
search_input = driver.find_element(By.ID, 'firstName')
search_input.send_keys('John')


search_input = driver.find_element(By.ID, 'lastName')
search_input.send_keys('Doe')

sleep(3)
search_input = driver.find_element(By.ID, 'userEmail')
search_input.send_keys("johndoe@example.com")

sleep(3)

# Закрываем браузер
driver.quit()
