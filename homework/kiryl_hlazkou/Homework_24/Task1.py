from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/select/single_select")


def test_submit():
    driver.find_element(By.ID, "id_choose_language").click()
    driver.find_element(By.XPATH, "//option[contains(text(),'Python')]").click()

    driver.find_element(By.ID, "submit-id-submit").click()

    result = driver.find_element(By.ID, "result-text")

    assert result.text == "Python"
