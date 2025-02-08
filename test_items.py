import time,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_of_button_exists(browser):
    button = False
    try:
        locator = EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
        button = WebDriverWait(browser, 1).until(locator)
    except:
        pass
    assert button, " Кнопка отсутствует на странице"
