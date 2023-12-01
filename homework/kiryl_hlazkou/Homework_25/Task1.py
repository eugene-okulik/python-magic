from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver


def test_shop(driver):
    driver.get("https://www.demoblaze.com/index.html")
    device = driver.find_element(By.XPATH, "//a[text()= 'Samsung galaxy s6']")
    # Open in a separate tab
    ActionChains(driver).key_down(Keys.CONTROL).click(device).key_up(Keys.CONTROL).perform()
    # Switch to second tab
    driver.switch_to.window(driver.window_handles[1])

    add_to_cart = driver.find_element(By.XPATH, "//a[text()= 'Add to cart']")
    add_to_cart.click()

    # Wait until alert outputs
    WebDriverWait(driver, 10).until(ec.alert_is_present())

    alert = Alert(driver)
    alert.accept()

    driver.close()

    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])

    # Open the Trash on the Start tab
    cart_link = driver.find_element(By.ID, "cartur")
    cart_link.click()

    # Make sure the item you added is in your cart
    added_item = driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']")
    assert added_item.text == "Samsung galaxy s6"

    # Close the browser
    driver.quit()
