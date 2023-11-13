import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_delivery_of_goods(driver):
    driver.get("https://www.demoblaze.com/index.html")
    item_link = driver.find_element(By.XPATH, '//a[contains(text(), "Samsung galaxy s6")]')
    item_link.click()
    time.sleep(2)
    main_window = driver.window_handles[0]

    # Добавление товара в корзину
    add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
    add_to_cart_button.click()
    time.sleep(2)

    driver.close()
    driver.switch_to.window(main_window)

    # Переход в транспортную корзину
    cart_button = driver.find_element(By.ID, "carter")
    cart_button.click()

    # Убедитесь, что в корзине находится добавленный товар
    cart_item = driver.find_element(By.XPATH, "//td[contains(text(), 'Samsung galaxy s6')]")
    assert cart_item is not None, "Товар не найден в корзине"

    driver.quit()
