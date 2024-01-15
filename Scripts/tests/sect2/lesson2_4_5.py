from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


def test_dif():
    try:
        browser = webdriver.Chrome()
        # говорим WebDriver ждать все элементы в течение 5 секунд
        browser.implicitly_wait(5)

        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        button = browser.find_element(By.ID, "book")
        price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
        button.click()

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text

        y = math.log(abs(12 * math.sin(int(x))))

        y_element = browser.find_element(By.ID, "answer")
        y_element.send_keys(str(y))

        # Отправляем заполненную форму

        buttonbtn = WebDriverWait(browser, 1).until(
            EC.element_to_be_clickable((By.ID, "solve"))
        )
        buttonbtn.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла