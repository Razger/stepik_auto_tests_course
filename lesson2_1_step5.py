from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time
import math


def test_dif():
    try:
        browser = webdriver.Chrome()
        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text

        y = math.log(abs(12*math.sin(int(x))))

        y_element = browser.find_element(By.ID, "answer")
        y_element.send_keys(str(y))

        chekbox_element = browser.find_element(By.ID, "robotCheckbox")
        browser.execute_script("return arguments[0].scrollIntoView(true);", chekbox_element)
        chekbox_element.click()

        radio_element = browser.find_element(By.ID, "robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radio_element)
        radio_element.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла