from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import pytest
import time
import math


def test_dif():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

        input_firstname = browser.find_element(By.NAME, "firstname")
        input_firstname.send_keys("Ivanov")

        input_lastname = browser.find_element(By.NAME, "lastname")
        input_lastname.send_keys("Ivan")

        input_email = browser.find_element(By.NAME, "email")
        input_email.send_keys("IvanIvanov@mail.ru")

        element_txt = browser.find_element(By.ID, "file")
        element_txt.send_keys(file_path)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
