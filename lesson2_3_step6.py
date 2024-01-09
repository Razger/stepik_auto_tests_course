from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time
import math


def test_dif():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text

        y = math.log(abs(12*math.sin(int(x))))

        y_element = browser.find_element(By.ID, "answer")
        y_element.send_keys(str(y))

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла