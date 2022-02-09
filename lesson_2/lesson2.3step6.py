from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


# --------Переключаемся на вкладки браузера
# --------new_window = browser.window_handles[1]
# возвращает массив имен, зная,что сейчас открыто две вкладки переходим на следюущую по индексу[1]
# browser.switch_to_window(new_window)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, 'button[class="trollface btn btn-primary"]')
    btn.click()
    #Получаем имя второй вкладки
    new_window = browser.window_handles[1]
    # Переключаем browser на новую вкладку
    browser.switch_to.window(new_window)
    digit = browser.find_element(By.ID, 'input_value').text
    x = calc(digit)

    input_zone = browser.find_element(By.NAME, 'text')
    input_zone.send_keys(x)

    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
