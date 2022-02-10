from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

# для запуска теста с терминале, находясь в папке с тестом
#pytest -s -v --browser_name=firefox test_cmd.py
