from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestValid(unittest.TestCase):
    def test_link1(self):
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get(link1)
        # Ваш код, который заполняет обязательные поля
        first_block = browser.find_element(By.CLASS_NAME, 'first_block')
        input1 = first_block.find_element(By.CLASS_NAME, "first")
        input1.send_keys("Ivan")
        input2 = first_block.find_element(By.CLASS_NAME, "second")
        input2.send_keys("Petrov")
        input3 = first_block.find_element(By.CLASS_NAME, "third")
        input3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        check_test = "Congratulations! You have successfully registered!"
        assert check_test == welcome_text
        self.assertEqual(check_test, welcome_text, f'Текст со страницы если задание выполнено: {welcome_text}, '
                                                   f'должен быть идентичен тексту: {check_test}')

    def test_link2(self):
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get(link2)
        # Ваш код, который заполняет обязательные поля
        first_block = browser.find_element(By.CLASS_NAME, 'first_block')
        input1 = first_block.find_element(By.CLASS_NAME, "first")
        input1.send_keys("Ivan")
        input2 = first_block.find_element(By.CLASS_NAME, "second")
        input2.send_keys("Petrov")
        input3 = first_block.find_element(By.CLASS_NAME, "third")
        input3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        check_test = "Congratulations! You have successfully registered!"
        assert check_test == welcome_text
        self.assertEqual(check_test, welcome_text, f'Текст со страницы если задание выполнено: {welcome_text}, '
                                                   f'должен быть идентичен тексту: {check_test}')


if __name__ == '__main__':
    unittest.main()
