"""
https://www.demoblaze.com/index.html
1. откройте товар в новой вкладке
2. Перейдите на вкладку с товаром
3. Добавьте товар в корзину
4. Закройте вкладку с товаром
5. На начальной вкладке откройте корзину
7. Убедитесь, что в корзине тот товар, который вы добавляли
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    # Initialize the Chrome WebDriver
    chrome_driver = webdriver.Chrome()
    # Maximize the window
    chrome_driver.maximize_window()
    return chrome_driver


def test_selected_product(driver):
    # Go to https://www.demoblaze.com/index.html
    driver.get('https://www.demoblaze.com/index.html')

    # 1. откройте товар в новой вкладке
    # Wait for the element
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='tbodyid']/div[1]/div[1]/a")))

    # Find the product link Samsung galaxy s6
    product_link = driver.find_element(By.XPATH, "//div[@id='tbodyid']/div[1]/div[1]/a")

    # Open the product link in a new tab using context_click (right-click)
    ActionChains(driver).key_down(Keys.CONTROL).click(product_link).key_up(Keys.CONTROL).perform()

    # 2. Перейдите на вкладку с товаром
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # 3. Добавьте товар в корзину
    # Wait for the "Add to cart" button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='tbodyid']/div[2]/div[1]/a")))

    # Add the product Samsung galaxy s6 to the cart
    driver.find_element(By.XPATH, "//div[@id='tbodyid']/div[2]/div[1]/a").click()

    # Wait for the alert to be present
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # accept the active alert
    alert = Alert(driver)
    alert.accept()

    # 4. Закройте вкладку с товаром
    # Close the tab with the product
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(tabs[0])

    # 5. На начальной вкладке откройте корзину
    driver.find_element(By.ID, 'cartur').click()

    # 6. Убедитесь, что в корзине тот товар, который вы добавляли
    # [.='Samsung galaxy s6']: Filters the selection to only include <td> elements
    # whose text content is exactly 'Samsung galaxy s6'.
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[.='Samsung galaxy s6']")))
    added_product = driver.find_element(By.XPATH, "//td[.='Samsung galaxy s6']")
    assert added_product.text == 'Samsung galaxy s6', 'Expected result: Samsung galaxy s6'
