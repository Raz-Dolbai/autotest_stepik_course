from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    click_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(1)
    allert_window = browser.switch_to.alert
    allert_window.accept()
    # получаем значение x для расчета и ввода в input
    x = browser.find_element(By.ID, 'input_value').text
    value_input = calc(x)
    input_tag = browser.find_element(By.TAG_NAME, 'input')
    input_tag.send_keys(value_input)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
