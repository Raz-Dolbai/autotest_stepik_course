from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_btn(browser):
    browser.get(link)
    x = browser.find_elements(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(x) > 0, 'Вы неверно выбрали элемент или искомая кнопка отсутствует'
