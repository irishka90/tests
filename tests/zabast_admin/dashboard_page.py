import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.zabast_admin.base_page import BasePage
from tests.zabast_admin.locators import BasePageLocators, NewsPageLocators, TextFields


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

    def edit_last_news(self):
        assert self.is_element_present(*BasePageLocators.DROP_DOWN)
        drop_down = self.browser.find_element(*BasePageLocators.DROP_DOWN)
        drop_down.click()
        time.sleep(1)
        assert self.is_element_present(*BasePageLocators.CHANGE_NEWS)
        change_news = self.browser.find_element(*BasePageLocators.CHANGE_NEWS)
        time.sleep(1)
        change_news.click()
        time.sleep(3)

        # замена даты
        assert self.is_element_present(*NewsPageLocators.CHOOSE_DATE), "chose-date area is not presented"
        date_area = self.browser.find_element(*NewsPageLocators.CHOOSE_DATE)
        date_area.clear()
        save_date = TextFields.yesterday
        date_area.send_keys(save_date)
        date_area.send_keys(Keys.RETURN)

        # замена заголовок-текст
        # 1 ru
        assert self.is_element_present(*NewsPageLocators.TITLE_1), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_1)
        title_area.clear()
        ru_title_2 = TextFields.title_ru_2
        title_area.send_keys(ru_title_2)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_1), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_1)
        content_area.clear()
        ru_content_2 = TextFields.content_ru_2
        content_area.send_keys(ru_content_2)
        time.sleep(2)

        # 2 en
        assert self.is_element_present(*NewsPageLocators.TITLE_2), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_2)
        title_area.clear()
        en_title_2 = TextFields.title_en_2
        title_area.send_keys(en_title_2)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_2), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_2)
        content_area.clear()
        en_content_2 = TextFields.content_en_2
        content_area.send_keys(en_content_2)
        time.sleep(2)

        # 3 es
        assert self.is_element_present(*NewsPageLocators.TITLE_3), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_3)
        title_area.clear()
        es_title_2 = TextFields.title_es_2
        title_area.send_keys(es_title_2)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_3), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_3)
        content_area.clear()
        es_content_2 = TextFields.content_es_2
        content_area.send_keys(es_content_2)
        time.sleep(2)

        # 4 de
        assert self.is_element_present(*NewsPageLocators.TITLE_4), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_4)
        title_area.clear()
        de_title_2 = TextFields.title_de_2
        title_area.send_keys(de_title_2)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_4), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_4)
        content_area.clear()
        de_content_2 = TextFields.content_de_2
        content_area.send_keys(de_content_2)
        time.sleep(2)

        # замена тэга
        assert self.is_element_present(*NewsPageLocators.TAG), "Tag area is not presented"
        tag_area = self.browser.find_element(*NewsPageLocators.TAG)

        tag_new = TextFields.tag_new
        tag_area.send_keys(tag_new)
        tag_area.send_keys(Keys.RETURN)

        assert self.is_element_present(*NewsPageLocators.CREATE_NEWS_BUTTON), "create button is not presented"
        create_news = self.browser.find_element(*NewsPageLocators.CREATE_NEWS_BUTTON)
        self.browser.execute_script('return arguments[0].scrollIntoView (true);', create_news)
        create_news.click()
        time.sleep(5)

        assert self.is_element_present(*BasePageLocators.DROP_DOWN)
        drop_down = self.browser.find_element(*BasePageLocators.DROP_DOWN)
        drop_down.click()
        time.sleep(1)
        assert self.is_element_present(*BasePageLocators.CHANGE_NEWS)
        change_news = self.browser.find_element(*BasePageLocators.CHANGE_NEWS)
        time.sleep(1)
        change_news.click()
        time.sleep(3)

        # проверка даты
        assert self.is_element_present(*NewsPageLocators.CHOOSE_DATE), "chose-date area is not presented"
        date_area = self.browser.find_element(*NewsPageLocators.CHOOSE_DATE)
        assert date_area.get_attribute('value') == save_date, "Not equal dates {} {}".format(
            date_area.get_attribute('value'), save_date)

        # Проверка заголовок-текст
        assert self.is_element_present(*NewsPageLocators.TITLE_1), "Title area is not presented"
        title_ru_area = self.browser.find_element(*NewsPageLocators.TITLE_1).get_attribute('value')
        assert ru_title_2 == title_ru_area, "Not equal ru_titles 1{} 2{}".format(ru_title_2, title_ru_area)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_1), "Content area is not presented"
        content_ru_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_1).get_attribute('value')
        assert ru_content_2 == content_ru_area, "Not equal ru_content 1{} 2{}".format(ru_content_2, content_ru_area)

        assert self.is_element_present(*NewsPageLocators.TITLE_2), "Title area is not presented"
        title_en_area = self.browser.find_element(*NewsPageLocators.TITLE_2).get_attribute('value')
        assert en_title_2 == title_en_area, "Not equal en_titles 1{} 2{}".format(en_title_2, title_en_area)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_2), "Content area is not presented"
        content_en_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_2).get_attribute('value')
        assert en_content_2 == content_en_area, "Not equal en_content 1{} 2{}".format(es_content_2, content_en_area)

        assert self.is_element_present(*NewsPageLocators.TITLE_3), "Title area is not presented"
        title_es_area = self.browser.find_element(*NewsPageLocators.TITLE_3).get_attribute('value')
        assert es_title_2 == title_es_area, "Not equal es_titles 1{} 2{}".format(en_title_2, title_es_area)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_3), "Content area is not presented"
        content_es_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_3).get_attribute('value')
        assert es_content_2 == content_es_area, "Not equal es_content 1{} 2{}".format(es_content_2, content_es_area)

        assert self.is_element_present(*NewsPageLocators.TITLE_4), "Title area is not presented"
        title_de_area = self.browser.find_element(*NewsPageLocators.TITLE_4).get_attribute('value')
        assert de_title_2 == title_de_area, "Not equal de_titles 1{} 2{}".format(de_title_2, title_de_area)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_4), "Content area is not presented"
        content_de_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_4).get_attribute('value')
        assert de_content_2 == content_de_area, "Not equal de_content 1{} 2{}".format(de_content_2, content_de_area)

        # проверка тега
        assert self.is_element_present(*NewsPageLocators.TAG_NEW), "Tag area is not presented"
        tag_area1 = self.browser.find_element(*NewsPageLocators.TAG_NEW).find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div/div[2]/form/div[7]/div/div/span[1]/span").text
        tag_area2 = self.browser.find_element(*NewsPageLocators.TAG_NEW).find_element(By.XPATH,
                                                                                  "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[7]/div/div/span[2]/span").text
        tag_area3 = self.browser.find_element(*NewsPageLocators.TAG_NEW).find_element(By.XPATH,
                                                                                  "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[7]/div/div/span[3]/span").text

        assert tag_new in tag_area1+tag_area2+tag_area3, "tag new {} is not in 1{} 2{} 3{}".format(tag_new, tag_area1, tag_area2, tag_area3)
