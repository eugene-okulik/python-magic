from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_product_comparison(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    # Наводим мышку на первый товар
    first_product = driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    compare = driver.find_element(By.XPATH, "//a[@title='Add to Compare']")
    ActionChains(driver).move_to_element(first_product).click(compare).perform()

    # Переходим на страницу сравнения товаров
    driver.find_element(By.XPATH, '//a[text()="comparison list"]').click()

    assert 'Push It Messenger Bag' in driver.page_source, "Товар  не добавлен в сравнение!"

    driver.quit()
