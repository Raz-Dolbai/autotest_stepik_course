from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/huge_form.html"

path = r'C:\Users\Maxim\Desktop\study\selenium_stepik_course\chromedriver'
try:
    browser = webdriver.Chrome(path)
    browser.get(link)
    all_link = browser.find_elements(By.TAG_NAME, 'input')
    for i in all_link:
        i.send_keys('fcuk')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла