from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_hello_world(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "button").click()
    driver.implicitly_wait(6)
    text = driver.find_element(By.XPATH, "//h4[normalize-space()='Hello World!']").text

    assert text == "Hello World!"
