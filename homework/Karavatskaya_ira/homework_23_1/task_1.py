from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(options=options)
driver.set_window_size(545, 867)
driver.get("https://demoqa.com/automation-practice-form")


def filling_out_the_form():
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
    phone_number.send_keys("1111111")

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()

    dropdown = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
    dropdown.click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
    dropdown.find_element(By.XPATH, "//option[. = '1999']").click()

    driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--012").click()

    sports = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(1) > .custom-control-label")
    sports.click()

    reading = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(2) > .custom-control-label")
    reading.click()

    music = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(3) > .custom-control-label")
    music.click()

    address = driver.find_element(By.ID, "currentAddress")
    address.click()
    address.send_keys("111, My adress, City, Country")

    state = driver.find_element(By.XPATH, "//div[@id='state']//div[@class="
                                          "' css-tlfecz-indicatorContainer']//*[name()='svg']")
    state.click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Uttar Pradesh')]").click()

    city = driver.find_element(By.XPATH, "//div[@id='city']//div[@class=' "
                                         "css-tlfecz-indicatorContainer']//*[name()='svg']")
    city.click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Lucknow')]").click()

    driver.find_element(By.ID, "submit").click()

    close = driver.find_element(By.XPATH, "//button[@id='closeLargeModal']")
    assert close.is_displayed()
