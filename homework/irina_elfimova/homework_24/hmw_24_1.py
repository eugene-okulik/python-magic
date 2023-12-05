from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(options=options)


def test_language_choice():
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    driver.set_window_size(1248, 1285)
    language = driver.find_element(By.ID, "id_choose_language")
    language.click()
    dropdown = driver.find_element(By.ID, "id_choose_language")
    dropdown.find_element(By.XPATH, "//option[. = 'JavaScript']").click()
    submit = driver.find_element(By.ID, "submit-id-submit")
    submit.click()
    selected_lg = driver.find_element(By.ID, "result-text").text
    assert selected_lg == "JavaScript"
