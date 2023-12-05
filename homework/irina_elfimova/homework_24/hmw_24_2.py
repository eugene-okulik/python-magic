from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(6)


def test_hello_world():
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.set_window_size(1248, 1285)
    start_button = driver.find_element(By.CSS_SELECTOR, "button")
    start_button.click()
    msg_text = driver.find_element(By.XPATH, "//h4[normalize-space()='Hello World!']").text
    assert msg_text == "Hello World!"
