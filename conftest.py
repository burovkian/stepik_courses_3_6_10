import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

lang_list=["ar","ca","cs","da","de","en-gb","el","es","fi","fr","it","ko","nl","pl","pt","pt-br","ro","ru","sk","uk","zh-cn"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose the language for page")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

def test_language_page(request):
    chosen_lang = request.config.getoption("language")
    if chosen_lang is None:
        raise pytest.UsageError(f"Choose the language for page from list: {lang_list}")
    else:
        link = f"http://selenium1py.pythonanywhere.com/{chosen_lang}/catalogue/coders-at-work_207/"
    return link

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.get(test_language_page(request))
    yield browser
    print("\nquit browser..")
    browser.quit()

