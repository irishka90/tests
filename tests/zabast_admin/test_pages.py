import time
import pytest
from selenium import webdriver

from tests.zabast_admin.base_page import BasePage, link
from tests.zabast_admin.event_page import EventPage
from tests.zabast_admin.news_page import NewsPage
from tests.zabast_admin.dashboard_page import DashboardPage


class TestLoginFrom():

    @pytest.fixture(scope="class")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.fixture(scope="function")
    def log_in(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_form()
        page.get_in()
        time.sleep(3)
        return browser

    @pytest.fixture(scope="function")
    def sorting(self, log_in):
        page = DashboardPage(log_in, link)
        page.sort_creating_date()
        return log_in

    @pytest.mark.users
    def test_log_out(self, log_in):
        page = BasePage(log_in, link)
        page.log_out()

    @pytest.mark.news
    def test_create_news(self, log_in):
        news_page = NewsPage(log_in, log_in.current_url)
        news_page.create_button()
        news_page.create_news()

    @pytest.mark.base
    def test_go_to_event_page(self, log_in):
        event_page = EventPage(log_in, link)
        event_page.go_to_event_page()

    @pytest.mark.events
    def test_create_event(self, log_in):
        event_page = EventPage(log_in, link)
        event_page.go_to_event_page()
        event_page.create_button()
        event_page.create_event()

    @pytest.mark.base
    def test_change_page(self, sorting):
        page = DashboardPage(sorting, link)
        page.change_page()

    @pytest.mark.news
    def test_delete_last_news(self, sorting):
        page = DashboardPage(sorting, link)
        page.delete_last_news()

    @pytest.mark.news
    def test_take_last_pub_away(self, sorting):
        page = DashboardPage(sorting, link)
        page.take_pub_away()
