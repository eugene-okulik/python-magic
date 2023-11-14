from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver


def test_delivery_of_goods(driver):
    driver.get("https://www.demoblaze.com/index.html")
    WebDriverWait(driver, 5)
    item_link = driver.find_element(By.XPATH, '//a[contains(text(), "Samsung galaxy s6")]')
    ActionChains(driver).key_down(Keys.CONTROL).click(item_link).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Добавление товара в корзину
    add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
    add_to_cart_button.click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()

    # Закрываем вкладку с товаром
    driver.close()

    # Возвращаемся на начальную вкладку
    driver.switch_to.window(tabs[0])

    # Переход в транспортную корзину
    cart_button = driver.find_element(By.ID, "cartur")
    cart_button.click()

    # Убедитесь, что в корзине находится добавленный товар
    cart_item = driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']")
    assert cart_item.text == 'Samsung galaxy s6'

    driver.quit()
