from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.implicitly_wait(6)


def test_hello():
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    result = driver.find_element(By.ID, "finish")

    assert result.text == "Hello World!"
