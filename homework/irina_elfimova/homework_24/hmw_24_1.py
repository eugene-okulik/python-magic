import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://www.qa-practice.com/elements/select/single_select")
        self.driver.set_window_size(1248, 1285)
        self.driver.find_element(By.ID, "id_choose_language").click()
        dropdown = self.driver.find_element(By.ID, "id_choose_language")
        dropdown.find_element(By.XPATH, "//option[. = 'JavaScript']").click()
        self.driver.find_element(By.ID, "submit-id-submit").click()
        self.driver.find_element(By.ID, "result-text").click()
        self.driver.find_element(By.ID, "result").click()
        self.driver.find_element(By.ID, "caret-down").click()
        self.driver.find_element(By.CSS_SELECTOR, "#caret-up > path").click()