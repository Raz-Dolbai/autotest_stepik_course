from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

#pytest-rerunfailures
#pip install pytest-rerunfailures - установка через pip
#в командной строке указываем количество прогонов упавших тестов –rerun
#Запуск из папки с тестом:
#pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
