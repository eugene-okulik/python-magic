from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.set_window_size(775, 900)
driver.get("https://demoqa.com/automation-practice-form")


def test_fill_forms():
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")

    second_name = driver.find_element(By.ID, "lastName")
    second_name.send_keys("Doe")

    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("johndoe@mail.com")

    gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    gender.click()

    mobile_number = driver.find_element(By.ID, "userNumber")
    mobile_number.send_keys("+37529000111")

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()

    dropdown = driver.find_element(By.CSS_SELECTOR, '[class="react-datepicker__year-select"]')
    dropdown.click()
    dropdown = driver.find_element(By.CSS_SELECTOR, '[class="react-datepicker__year-select"]')
    dropdown.find_element(By.XPATH, "//option[. = '1999']").click()

    driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--018").click()

    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()

    address = driver.find_element(By.CSS_SELECTOR, '[placeholder="Current Address"]')
    address.click()
    address.send_keys("Address")

    state = driver.find_element(By.XPATH, '//*[@id="state"]')
    state.click()
    driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()

    city = driver.find_element(By.XPATH, '//*[@id="city"]')
    city.click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()

    driver.find_element(By.ID, "submit").click()
