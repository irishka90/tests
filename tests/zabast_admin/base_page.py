import datetime
import time

from selenium.common.exceptions import NoSuchElementException

from tests.zabast_admin.locators import BasePageLocators

link = "http://104.248.35.86/moderation/#/login"


class BasePage():

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://104.248.35.86/moderation", \
            "link is not correct "

    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not presented"
        time.sleep(7)

    def log_out(self):
        assert self.is_element_present(*BasePageLocators.LOG_OUT), "Log-out button not found"
        get_out = self.browser.find_element(*BasePageLocators.LOG_OUT)
        get_out.click()
        out_button = self.browser.find_element(*BasePageLocators.OUT_BUTTON)
        out_button.click()
        time.sleep(3)

    def change_page(self):
        assert self.is_element_present(*BasePageLocators.FORWARD_BUTTON), "Forward button not found"
        one_page_forward = self.browser.find_element(*BasePageLocators.FORWARD_BUTTON)
        one_page_forward.click()
        assert self.is_element_present(*BasePageLocators.BACK_BUTTON), "Back button not found"
        one_page_back = self.browser.find_element(*BasePageLocators.BACK_BUTTON)
        one_page_back.click()
        assert self.is_element_present(*BasePageLocators.CHOOSE_PAGE_3), "page 3 button not found"
        one_page_back = self.browser.find_element(*BasePageLocators.CHOOSE_PAGE_3)
        one_page_back.click()

    def get_in(self, email="admin_tester@gmail.com", password="q1w2e3r4"):
        assert self.is_element_present(*BasePageLocators.LOGIN_INPUT), "Not found email input"
        email_input = self.browser.find_element(*BasePageLocators.LOGIN_INPUT)
        email_input.send_keys(email)
        assert self.is_element_present(*BasePageLocators.PASSWORD_INPUT), "Not found password1 input"
        password_1 = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_1.send_keys(password)
        assert self.is_element_present(*BasePageLocators.REG_SUBMIT), "Not found button registration"
        button_submit = self.browser.find_element(*BasePageLocators.REG_SUBMIT)
        button_submit.click()
        time.sleep(7)

    def sort_creating_date(self):
        assert self.is_element_present(*BasePageLocators.DATA_TABLE_SORTING)
        table = self.browser.find_element(*BasePageLocators.DATA_TABLE_SORTING) \
            .find_elements_by_class_name("baseTable__row")
        assert len(table) > 0, "No events or news"

        assert self.is_element_present(*BasePageLocators.DATE_SORTING), "No sort element"

        sort = self.browser.find_element(*BasePageLocators.DATE_SORTING)
        sort.click()
        assert self.is_element_present(*BasePageLocators.DATE_SORTING_ASC), "No ASC mode"
        self.check_asc_desc(mode=True)

        sort = self.browser.find_element(*BasePageLocators.DATE_SORTING)
        sort.click()
        assert self.is_element_present(*BasePageLocators.DATE_SORTING_DESC), "No DESC mode"
        self.check_asc_desc(mode=False)

        time.sleep(3)

    def check_asc_desc(self, mode):
        table = self.browser.find_element(*BasePageLocators.DATA_TABLE_SORTING) \
            .find_elements_by_class_name("baseTable__row")

        first = table[0].find_elements_by_class_name("baseTable__cell")[2].find_element_by_tag_name("span").text
        second = table[1].find_elements_by_class_name("baseTable__cell")[2].find_element_by_tag_name("span").text
        timeFirst = time.mktime(datetime.datetime.strptime(first, "%d-%m-%Y %H:%M").timetuple())
        timeSecond = time.mktime(datetime.datetime.strptime(second, "%d-%m-%Y %H:%M").timetuple())

        if mode:
            assert timeFirst <= timeSecond, "No sort ASC mode"
        else:
            assert timeFirst >= timeSecond, "No sort DESC mode"

    def delete_last_news(self):
        assert self.is_element_present(*BasePageLocators.DROP_DOWN)
        drop_down = self.browser.find_element(*BasePageLocators.DROP_DOWN)
        drop_down.click()
        assert self.is_element_present(*BasePageLocators.DELETE_NEWS)
        del_news = self.browser.find_element(*BasePageLocators.DELETE_NEWS)
        del_news.click()
        assert self.is_element_present(*BasePageLocators.DELETE_NEWS_OK)
        del_news_ok = self.browser.find_element(*BasePageLocators.DELETE_NEWS_OK)
        del_news_ok.click()

    def take_pub_away(self):
        assert self.is_element_present(*BasePageLocators.DROP_DOWN)
        drop_down = self.browser.find_element(*BasePageLocators.DROP_DOWN)
        drop_down.click()
        assert self.is_element_present(*BasePageLocators.TAKE_AWAY)
        del_news = self.browser.find_element(*BasePageLocators.TAKE_AWAY)
        del_news.click()
        time.sleep(5)
        assert self.is_element_present(*BasePageLocators.TAKE_AWAY_OK)
        del_news_ok = self.browser.find_element(*BasePageLocators.TAKE_AWAY_OK)
        del_news_ok.click()
        time.sleep(8)
