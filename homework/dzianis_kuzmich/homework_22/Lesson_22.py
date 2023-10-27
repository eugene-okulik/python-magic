from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep


options = Options()
# options.add_argument('start-maximized')
# options.add_argument('--window-size=500,1080')
# options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
# driver.quit()
sleep(3)
driver.maximize_window()
# driver.set_window_size(500, 1080)
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('cat')
search_input.send_keys(Keys.RETURN)

sleep(4)

if driver.title.startswith("cat"):
    print("Title starts with 'cat'!")
else:
    print(f"Title does not start with 'cat'. Title is: {driver.title}")

driver.quit()
