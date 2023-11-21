from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_product_comparison(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    device = driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    compare = driver.find_element(By.XPATH, "//a[@title='Add to Compare']")
    # Move to compare element
    ActionChains(driver).move_to_element(device).click(compare).perform()

    # Wait until compare list element outputs
    wait = WebDriverWait(driver, 10)
    comparison_link = wait.until(
        ec.element_to_be_clickable((By.XPATH, '//a[(text()="comparison list")]'))
        )
    comparison_link.click()

    added_device = driver.find_element(By.XPATH, "//strong//a[@title='Push It Messenger Bag']")
    assert added_device.text == 'Push It Messenger Bag'

    driver.quit()
