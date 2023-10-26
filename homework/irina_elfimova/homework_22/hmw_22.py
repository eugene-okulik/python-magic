from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/')


def test_tittle_page():
    driver.find_element(By.NAME, 'q').send_keys('cat')
    driver.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
    get_title = driver.title
    assert get_title == 'cat - Поиск в Google'
    print(get_title)
