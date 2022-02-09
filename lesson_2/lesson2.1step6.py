from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #Считываем значение x
    x_element = browser.find_element(By.TAG_NAME, 'img')
    x = x_element.get_attribute('valuex')
    x = calc(x)
    input_x = browser.find_element(By.ID, 'answer')
    input_x.send_keys(x)
    check_click = browser.find_element(By.ID, "robotCheckbox")
    check_click.click()
    robot = browser.find_element(By.ID, "robotsRule")
    robot.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
