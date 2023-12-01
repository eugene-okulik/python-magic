from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/select/single_select")


def test_submit():
    dropdown = driver.find_element(By.ID, "id_choose_language")
    select = Select(dropdown)
    select.select_by_visible_text("Python")

    driver.find_element(By.ID, "submit-id-submit").click()

    result = driver.find_element(By.ID, "result-text")

    assert result.text == "Python"
