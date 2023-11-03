from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('cat')
search_input.send_keys(Keys.RETURN)


assert driver.title.startswith("cat")

driver.quit()
