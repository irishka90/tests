import time

import pytest
from selenium import webdriver

link = "https://strikeapi.herokuapp.com"


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def open_main(browser):
    browser.get(link)
    time.sleep(5)


@pytest.fixture(scope="function")
def base_tab_news(browser):
    news = browser.find_element_by_xpath("/html/body/div/section/header/div/div[2]/ul/li[2]")
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
    button = browser.find_element_by_class_name("el-button.authSectionDialogForm__button.el-button--primary")
    button.click()
    time.sleep(2)

@pytest.fixture(scope="function")
def registration_twitter(browser):
    button = browser.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/ul/div/button")
    button.click()
    button=browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/div[1]/button[2]")
    button.click()
    input_1=browser.find_element_by_xpath("/html/body/div[2]/div/form/fieldset[1]/div[1]/input")
    input_1.send_keys("???")
    input_2 = browser.find_element_by_xpath("/html/body/div[2]/div/form/fieldset[1]/div[2]/input")
    input_2.send_keys("???")
    button = browser.find_element_by_id("allow")
    button.click()
    time.sleep(2)

    time.sleep(2)


@pytest.fixture(scope="function")
def scroll_window(browser):
    browser.execute_script("window.scrollBy(0,600);")


class TestZabast():
    def test_news(self, browser, open_main, base_tab_news):
        tab = browser.find_element_by_class_name("el-menu-item.headerNav__item.is-active")
        assert base_tab_news == tab, "Нет"

    def test_news_read(self, browser, open_main, base_tab_news):
        read_news = browser.find_element_by_id("item-385")
        header_text_1 = browser.find_element_by_xpath(
            "/html/body/div/section/main/div/div/div/div[2]/div[1]/div/h2").text
        read_news.click()
        time.sleep(3)
        header_text_2 = browser.find_element_by_xpath("/html/body/div/section/main/div/div/div[1]/h2").text
        assert header_text_1 == header_text_2, "не та новость"

    def test_comment(self, browser, open_main, registration_with_login, base_tab_news, scroll_window):
        tab = browser.find_element_by_class_name("el-menu-item.headerNav__item.is-active")
        time.sleep(5)
        read_news = browser.find_element_by_id("item-385")
        read_news.click()
        time.sleep(3)
        input_comment = browser.find_element_by_xpath("/html/body/div/section/main/div/div/div[2]/div[3]/div/textarea")
        comment_text = input_comment.send_keys("тест-проверка")
        button = browser.find_element_by_class_name(
            "el-button.baseComments__sendButton.el-button--default.el-button--medium")
        button.click()
        time.sleep(5)
        comment = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[2]/div[2]/div[1]/div[2]/p").text
        #assert comment == comment_text, "не совпадает"

    def test_delete_comment(self, browser, open_main, registration_with_login, base_tab_news, scroll_window):
        tab = browser.find_element_by_class_name("el-menu-item.headerNav__item.is-active")
        time.sleep(5)
        read_news = browser.find_element_by_id("item-385")
        read_news.click()
        time.sleep(3)
        delete = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/a/span")
        delete.click()
        time.sleep(3)
        button = browser.find_element_by_class_name("el-button.el-button--default.el-button--small.el-button--primary")
        button.click()
        time.sleep(5)
        #assert

    def test_map_view(self, browser, open_main, registration_with_login):
        map = browser.find_element_by_xpath("/html/body/div/section/header/div/div[2]/ul/li[3]")
        map.click()
        time.sleep(5)
        return map
