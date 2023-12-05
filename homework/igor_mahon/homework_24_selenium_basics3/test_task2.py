"""
Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2,
нажмет Start, и проверит, что на странице появляется текст "Hello World!
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    # Initialize the Chrome WebDriver
    chrome_driver = webdriver.Chrome()
    # Maximize the window
    chrome_driver.maximize_window()
    return chrome_driver


def test_selected_value1(driver):
    # Go to https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    # Locate the button Start and click
    driver.find_element(By.XPATH, "//div[@id='start']/button").click()
    # Locate, wait and save the outputted element in the variable
    submit_button = (
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
    )
    assert submit_button.text == 'Hello World!', 'Expected result: Hello World!'
