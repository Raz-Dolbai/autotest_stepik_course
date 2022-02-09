from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_link_text"

path = r'C:\Users\Maxim\Desktop\study\selenium_stepik_course\chromedriver'
try:
    browser = webdriver.Chrome(path)
    browser.get(link)
    time.sleep(2)
    digit = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(digit)
    link_text = browser.find_element(By.PARTIAL_LINK_TEXT, digit)
    link_text.click()
    time.sleep(1)
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла