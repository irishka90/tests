import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
link = "https://strikeapi.herokuapp.com"

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language:  ru, en and etc.")

@pytest.fixture(scope="class")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def open_main(browser):
    browser.get(link)
    time.sleep(5)


@pytest.fixture(scope="function")
def base_tab_news(browser):
    news = browser.find_element_by_class_name("headerNavItem__text")
    news.click()
    time.sleep(2)
    return news


@pytest.fixture(scope="function")
def registration_with_login(browser):
    button = browser.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/ul/div/button")
    button.click()
    input_1 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[3]/input")
    input_1.send_keys("test@test.test")
    input_2 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[4]/input")
    input_2.send_keys("qwe123")
    button = browser.find_element_by_class_name("el-button--primary")
    button.click()
    time.sleep(2)


@pytest.fixture(scope="function")
def registration_twitter(browser):
    button = browser.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/ul/div/button")
    button.click()
    button = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/div[1]/button[2]")
    button.click()
    input_1 = browser.find_element_by_xpath("/html/body/div[2]/div/form/fieldset[1]/div[1]/input")
    input_1.send_keys("???")
    input_2 = browser.find_element_by_xpath("/html/body/div[2]/div/form/fieldset[1]/div[2]/input")
    input_2.send_keys("???")
    button = browser.find_element_by_id("allow")
    button.click()
    time.sleep(2)


@pytest.fixture(scope="function")
def scroll_window(browser):
    browser.execute_script("window.scrollBy(0,600);")


