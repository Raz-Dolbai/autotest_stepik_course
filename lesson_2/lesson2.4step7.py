from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# У элемента на странице могут быть разные свойства типа
#
# Кнопка может быть неактивной, то есть её нельзя кликнуть;
# Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
# Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.

try:
    options = ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    digit = browser.find_element(By.ID, 'input_value').text
    x = calc(digit)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.ID, 'solve').click()



finally:
    time.sleep(10)
    browser.quit()
