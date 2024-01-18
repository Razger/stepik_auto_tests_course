import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://stepik.org/lesson/236895/step/1"

stepik_login = ""
stepik_password = ""

list_link = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]


def login_funct(browser):
    button_login = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
    button_login.click()
    login = browser.find_element(By.NAME, "login")
    login.send_keys(stepik_login)
    password = browser.find_element(By.NAME, "password")
    password.send_keys(stepik_password)
    button_sign = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button_sign.click()
    time.sleep(5)


class TestLoginPage:

    @pytest.mark.parametrize("list_link", list_link)
    def test_input_and_read_answer(self, browser, list_link):
        browser.implicitly_wait(15)
        browser.get(list_link)

        login_funct(browser)

        answer = math.log(int(time.time()))
        input_answer = browser.find_element(By.CLASS_NAME, "ember-text-area")
        input_answer.send_keys(answer)
        button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
        button_send.click()
        time.sleep(10)
        fidback_text_elt = browser.find_element(By.CLASS_NAME, "smart-hints")
        fidback_text = fidback_text_elt.text
        exep_fid_text = "Correct!"
        assert fidback_text == exep_fid_text, f"Ожидалось {exep_fid_text}, получили {fidback_text}"

