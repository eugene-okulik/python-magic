from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(options=options)


def test_untitled():
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    driver.set_window_size(1248, 1285)
    driver.find_element(By.ID, "id_choose_language").click()
    dropdown = driver.find_element(By.ID, "id_choose_language")
    dropdown.find_element(By.XPATH, "//option[. = 'JavaScript']").click()
    driver.find_element(By.ID, "submit-id-submit").click()
    selected_lg = driver.find_element(By.ID, "result-text").text
    assert selected_lg == "JavaScript"
