import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


class TestLoginPage():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.implicitly_wait(5)
        browser.get(link)
        time.sleep(1)
        button_login = browser.find_element(By.CSS_SELECTOR, "#ember33")
        button_login.click()
        login = browser.find_element(By.NAME, "login")
        login.send_keys("login")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("password")

        button_sign = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        button_sign.click()
        time.sleep(15)
