from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/')


def test_get_tittle():
    driver.find_element(By.NAME, 'q').send_keys('cat')
    driver.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
    title = driver.title
    assert title.startswith('cat')
