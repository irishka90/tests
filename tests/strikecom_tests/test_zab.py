import time

import pytest
from selenium import webdriver

link = "https://strikeapi.herokuapp.com"


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="class")
def open_main(browser):
    browser.get(link)
    time.sleep(5)


@pytest.fixture(scope="class")
def base_tab_news(browser):
    news = browser.find_element_by_xpath("/html/body/div/section/header/div/div[2]/ul/li[2]")
    news.click()
    time.sleep(2)
    return news


class TestZabast():
    def test_news(self, browser, open_main, base_tab_news):
        tab = browser.find_element_by_class_name("el-menu-item.headerNav__item.is-active")
        assert base_tab_news == tab, "Нет"

    def test_news_read(self, browser, open_main, base_tab_news):
        #    base_tab_news(browser)
        read_news = browser.find_element_by_id("item-385")
        header_text_1 = browser.find_element_by_xpath(
            "/html/body/div/section/main/div/div/div/div[2]/div[1]/div/h2").text
        read_news.click()
        time.sleep(3)
        header_text_2 = browser.find_element_by_xpath("/html/body/div/section/main/div/div/div[1]/h2").text
        assert header_text_1 == header_text_2, "не та новость"
