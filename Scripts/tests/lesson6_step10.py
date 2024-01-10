from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math


def test_dif():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element_first = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        element_first.send_keys("Ivan")
        element_second = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        element_second.send_keys("Ivanov")
        element_third = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        element_third.send_keys("IvanIvanov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла