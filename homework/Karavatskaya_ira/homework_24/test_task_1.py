from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_select_option(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    # Выбор опции из выпадающего списка
    select = driver.find_element(By.ID, "id_choose_language")
    select.click()
    dropdown = driver.find_element(By.ID, "id_choose_language")
    dropdown.find_element(By.XPATH, "//option[. = 'Python']").click()

    # Клик на кнопке Submit
    driver.find_element(By.ID, "submit-id-submit").click()

    # Получение текста из окна с результатом
    result_text = driver.find_element(By.ID, "result-text").text

    # Вывод результата
    print("Выбранный вариант:", result_text)
    assert result_text == "Python"

    # Закрытие браузера
    driver.quit()
