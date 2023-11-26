"""
Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет, что в окошке с результатом отображается
тот вариант, который был выбран.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    # Initialize the Chrome WebDriver
    chrome_driver = webdriver.Chrome()
    # Maximize the window
    chrome_driver.maximize_window()
    return chrome_driver


def test_selected_value(driver):
    # Go to https://www.qa-practice.com/elements/select/single_select
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    # Locate the input field by ID and click
    driver.find_element(By.ID, 'id_choose_language').click()
    # Locate the second value in the picklist by XPATH and click
    driver.find_element(By.XPATH, "//div[@id='div_id_choose_language']/select/option[2]").click()
    # Locate the button Submit and click
    driver.find_element(By.ID, 'submit-id-submit').click()
    # Locate and save the outputted element in the variable
    value = driver.find_element(By.ID, 'result-text')
    assert value.text == 'Python', 'Expected result: Python'
