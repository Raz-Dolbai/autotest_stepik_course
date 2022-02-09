import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ссылки параметры для передачи в фикстуру
all_links = ['https://stepik.org/lesson/236895/step/1',
             'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1',
             'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1',
             'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1',
             'https://stepik.org/lesson/236905/step/1']

sentences = ''


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    print(f'\n{sentences}')


class TestPage():
    # Переменная для хранения строки

    @pytest.mark.parametrize('links', all_links)
    def test_correct_input(self, browser, links):
        global sentences
        link = links
        browser.get(link)
        answer = str(math.log(int(time.time())))
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
        text_message = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))).text
        try:
            assert text_message == 'Correct!', f'{text_message} должен быть равен Correct!'
        except AssertionError:
            sentences += text_message
