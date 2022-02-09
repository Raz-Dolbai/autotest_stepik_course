import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print('browser start')
    browser = webdriver.Firefox()
    browser.get("https://stepik.org/lesson/25969/step/8")
    yield browser
    browser.quit()
    print('browser quit')

