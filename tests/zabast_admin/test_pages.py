import time
import pytest
from selenium import webdriver

from tests.zabast_admin.base_page import BasePage, link
from tests.zabast_admin.event_page import EventPage
from tests.zabast_admin.news_page import NewsPage


class TestLoginFrom():

    @pytest.fixture(scope="class")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    def test_go_to_news_page_from_login_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        time.sleep(3)


    def test_log_out(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        time.sleep(3)
        page.log_out()


    def test_create_news(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        time.sleep(1)
        news_page = NewsPage(browser, browser.current_url)
        news_page.create_button()
        news_page.create_news()

    def test_go_to_event_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        event_page = EventPage(browser, link)
        event_page.go_to_event_page()

    def test_create_event(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        event_page = EventPage(browser, link)
        event_page.go_to_event_page()
        event_page.create_button()
        event_page.create_event()

    def test_change_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        page.sort_creating_date()
        page.change_page()
        time.sleep(2)

    def test_sorting(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        page.sort_creating_date()

    def test_delete_last_news(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        page.sort_creating_date()
        page.delete_last_news()

    def test_take__last_pub_away(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        page.sort_creating_date()
        page.take_pub_away()
