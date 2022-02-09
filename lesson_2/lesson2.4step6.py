from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

# --------Тут про замену time.sleep, есть способ лучше


try:
    options = ChromeOptions()
    browser = webdriver.Chrome(options=options)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    link = 'http://suninjuly.github.io/wait1.html'
    link2 = 'http://suninjuly.github.io/cats.html'
    browser.get(link2)
    browser.find_element(By.ID, "button")

    btn = browser.find_element(By.ID, 'verify').click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(2)
    browser.quit()
