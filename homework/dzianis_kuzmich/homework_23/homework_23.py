from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
driver = webdriver.Chrome(options=options)
driver.set_window_size(585, 1266)
driver.get('https://demoqa.com/automation-practice-form')


def test_fill_out_form():
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.click()
    first_name.send_keys('John')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.click()
    last_name.send_keys('Doe')

    email = driver.find_element(By.ID, 'userEmail')
    email.click()
    email.send_keys('johndoe@gmail.com')

    gender = driver.find_element(By.CSS_SELECTOR, '.custom-radio:nth-child(1) > .custom-control-label')
    gender.click()

    mobile = driver.find_element(By.ID, 'userNumber')
    mobile.click()
    mobile.send_keys('911')

    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()

    dropdown = driver.find_element(By.XPATH, "//div[@aria-label='Choose Monday, November 6th, 2023']")
    dropdown.click()

    sports = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(1) > .custom-control-label")
    sports.click()

    music = driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(3) > .custom-control-label")
    music.click()

    address = driver.find_element(By.ID, "currentAddress")
    address.click()
    address.send_keys("Ventura Blvd")

    state = driver.find_element(By.XPATH, "//div[@id='stateCity-wrapper']//div[3]")
    state.click()

    city = driver.find_element(By.XPATH, "//div[@class='text-right col-md-2 col-sm-12']")
    city.click()

    driver.find_element(By.ID, "submit").click()
    close = driver.find_element(By.XPATH, "//button[@id='closeLargeModal']")
    assert close.is_displayed()
