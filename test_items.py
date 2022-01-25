"""
Модуль по заданию 3-6-9.
Поиск кнопки на странице с передачей параметров языка
"""
import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_basket(browser):
    """
    Поиск кнопки "Добавить в корзину"
    """
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, 'Кнопка не найдена!'
