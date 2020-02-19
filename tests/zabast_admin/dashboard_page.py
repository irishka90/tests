import datetime
import time

from selenium.webdriver.common.by import By

from tests.zabast_admin.base_page import BasePage
from tests.zabast_admin.locators import BasePageLocators


class DashboardPage(BasePage):

    def change_page(self):

        nmbr1 = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        assert self.is_element_present(*BasePageLocators.FORWARD_BUTTON), "Forward button not found"
        one_page_forward = self.browser.find_element(*BasePageLocators.FORWARD_BUTTON)
        one_page_forward.click()

        nmbr2 = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        print("1st ID on page 1:", nmbr1)
        print("1st ID on page 2:", nmbr2)
        assert nmbr1 != nmbr2, "page not changed to №2"

        assert self.is_element_present(*BasePageLocators.BACK_BUTTON), "Back button not found"
        one_page_back = self.browser.find_element(*BasePageLocators.BACK_BUTTON)
        one_page_back.click()
        nmbr3 = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        print("1st ID on page 2:", nmbr2)
        print("1st ID on page 1:", nmbr3)
        assert nmbr3 != nmbr2, "page not changed to №1"

        assert self.is_element_present(*BasePageLocators.CHOOSE_PAGE_3), "page 3 button not found"
        one_page_back = self.browser.find_element(*BasePageLocators.CHOOSE_PAGE_3)
        one_page_back.click()
        nmbr4 = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        print("1st ID on page 1:", nmbr3)
        print("1st ID on page 3:", nmbr4)
        assert nmbr3 != nmbr4, "page not changed to №3"

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
        first_id_on_page = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        second_id_on_page = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[1] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        assert self.is_element_present(*BasePageLocators.DROP_DOWN)
        drop_down = self.browser.find_element(*BasePageLocators.DROP_DOWN)
        drop_down.click()
        time.sleep(1)
        assert self.is_element_present(*BasePageLocators.DELETE_NEWS)
        del_news = self.browser.find_element(*BasePageLocators.DELETE_NEWS)
        del_news.click()
        time.sleep(1)
        assert self.is_element_present(*BasePageLocators.DELETE_NEWS_OK)
        del_news_ok = self.browser.find_element(*BasePageLocators.DELETE_NEWS_OK)
        del_news_ok.click()
        time.sleep(3)
        first_id_on_page_after_del = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text

        print(first_id_on_page)
        print(second_id_on_page)
        print(first_id_on_page_after_del)
        assert first_id_on_page_after_del == second_id_on_page, "not successfull remove"

    def take_pub_away(self):

        status = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[4] \
            .is_element_present(By.CLASS_NAME, "publicationStatusCell__icon.--close")

        assert self.is_element_present(*BasePageLocators.DROP_DOWN)
        drop_down = self.browser.find_element(*BasePageLocators.DROP_DOWN)
        time.sleep(1)
        drop_down.click()
        assert self.is_element_present(*BasePageLocators.TAKE_AWAY)
        del_news = self.browser.find_element(*BasePageLocators.TAKE_AWAY)
        time.sleep(1)
        del_news.click()
        time.sleep(3)
        assert self.is_element_present(*BasePageLocators.TAKE_AWAY_OK)
        take_away_ok = self.browser.find_element(*BasePageLocators.TAKE_AWAY_OK)
        time.sleep(1)
        take_away_ok.click()

        status_changed = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[4] \
            .is_element_present(By.CLASS_NAME, "publicationStatusCell__icon.--close")

        assert status != status_changed, "publication not taken away"
