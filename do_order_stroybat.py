from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

try:
    link = "https://stroybat.ru/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    browser.maximize_window()

    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input_art = browser.find_element(By.TAG_NAME, 'input[name="search_string"]')
    input_art.send_keys('400010')
    find_code = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    find_code.click()
    find_btn_basket = browser.find_element(By.CSS_SELECTOR,
                                           'button[class = "btn btn-default green small buy-btn add_basket"]')
    find_btn_basket.click()
    price = browser.find_element(By.CLASS_NAME, 'num.price_goods').text
    # Переходит в корзину
    find_go_to_basket = browser.find_element(By.XPATH, '//a[text()="Перейти в корзину"]')
    find_go_to_basket.click()
    # ----------------Корзина---------------------------------------------------------------
    # Нажимаем на купить в 1 клик
    button_buy_1click = browser.find_element(By.XPATH, '//button[text()="Купить в 1 клик"]')
    button_buy_1click.click()
    # Отрабатываем пупам купить в 1 клик
    popup = browser.find_element(By.CSS_SELECTOR, 'div.popup.order_popup')
    input_name = popup.find_element(By.TAG_NAME, 'input[class = "form-control green required name bround"]')
    input_name.send_keys('Desiptikon')
    input_phone = popup.find_element(By.TAG_NAME, 'input[class = "form-control green required phone bround"]')
    input_phone.send_keys('9001111111')
    input_mail = popup.find_element(By.TAG_NAME, 'input[class = "form-control green required email bround"]')
    input_mail.send_keys('kiss_me@mail.ru')

    btn = popup.find_element(By.CSS_SELECTOR, 'button[class="btn btn-default small green"]')
    btn.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
