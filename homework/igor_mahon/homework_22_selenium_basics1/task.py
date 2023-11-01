import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google_cat_search(driver):
    # Зайти на https://www.google.com/
    driver.get('https://www.google.com/')

    # Находим поле ввода и введим "cat" строку поиска
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('cat')
    sleep(1)  # без этого тест падает, в дальнейших тестах на буду использовать sleep :)

    # Нажать кнопку "Поиск в Google"
    search_button = driver.find_element(By.NAME, 'btnK')
    search_button.click()

    # Получаем заголовок title открытой страницы
    search_results_title = driver.title
    print(search_results_title)

    # В результате поиска проверить, что у открывшейся страницы title начинается со слова "cat"
    assert search_results_title.startswith('cat')
