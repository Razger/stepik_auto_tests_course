from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math
import unittest


class TestAbs(unittest.TestCase):
    def test_check_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            element_first_first = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
            element_first_first.send_keys("Ivan")
            element_first_second = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
            element_first_second.send_keys("Ivanov")
            element_first_third = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
            element_first_third.send_keys("IvanIvanov@mail.ru")
            element_second_first = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
            element_second_first.send_keys("+79994445522")
            element_second_third = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
            element_second_third.send_keys("Moscow, New-Station, 11/4")

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

            exceptet_text = "Congratulations! You have successfully registered!"
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(exceptet_text, welcome_text,
                             f"Текст не соответствует ожидаемому, "
                             f"Ожидалось {exceptet_text},"
                             f"Пришло {welcome_text}")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_check_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            element_first_first = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
            element_first_first.send_keys("Ivan")
            element_first_second = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
            element_first_second.send_keys("IvanIvanov@mail.ru")
            element_second_first = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
            element_second_first.send_keys("+79994445522")
            element_second_third = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
            element_second_third.send_keys("Moscow, New-Station, 11/4")

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

            exceptet_text = "Congratulations! You have successfully registered!"
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(exceptet_text, welcome_text,
                             f"Текст не соответствует ожидаемому, "
                             f"Ожидалось {exceptet_text},"
                             f"Пришло {welcome_text}")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
