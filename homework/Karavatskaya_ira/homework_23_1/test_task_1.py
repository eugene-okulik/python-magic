from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_filling_out_the_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    first_name = driver.find_element(By.ID, "firstName")
    first_name.click()
    first_name.send_keys("Vadim")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.click()
    last_name.send_keys("Petrov")

    email = driver.find_element(By.ID, "userEmail")
    email.click()
    email.send_keys("petrov_test@gmail.com")

    gender = driver.find_element(By.CSS_SELECTOR, ".custom-radio:nth-child(2) > .custom-control-label")
    gender.click()

    phone_number = driver.find_element(By.ID, "userNumber")
    phone_number.click()
    phone_number.send_keys("375293914623")

    actions = ActionChains(driver)
    input_subject = driver.find_element(By.XPATH, "//div[@id='subjectsWrapper']/div[2]/div[1]/div[1]/div[1]")
    actions.click(input_subject).send_keys('NEW SUBJECT!').perform()

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()

    driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--012").click()

    sports = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(1) > .custom-control-label")
    sports.click()

    reading = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(2) > .custom-control-label")
    reading.click()

    music = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(3) > .custom-control-label")
    music.click()

    driver.find_element(By.ID, "currentAddress").send_keys("111, City, Country")

    state = driver.find_element(By.XPATH, '//div[@id="state"]/div/div[2]')

    driver.execute_script("arguments[0].scrollIntoView();", state)
    actions.click(state).send_keys(Keys.ENTER).perform()

    city = driver.find_element(By.XPATH, '//div[@id="city"]/div/div[2]')
    actions.click(city).send_keys(Keys.ENTER).perform()

    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    close = driver.find_element(By.XPATH, "//button[@id='closeLargeModal']")
    assert close.is_displayed()
