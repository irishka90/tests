import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.zabast_admin.base_page import BasePage
from tests.zabast_admin.locators import NewsPageLocators, TextFields


class NewsPage(BasePage):
    def create_button(self):
        assert self.is_element_present(*NewsPageLocators.CREATE_BUTTON), "Create-button is not presented"
        button_submit = self.browser.find_element(*NewsPageLocators.CREATE_BUTTON)
        button_submit.click()
        time.sleep(3)

    def create_news(self):
        assert self.is_element_present(*NewsPageLocators.CHOOSE_DATE), "chose-date area is not presented"
        date_area = self.browser.find_element(*NewsPageLocators.CHOOSE_DATE)
        date_area.send_keys(TextFields.date)
        date_area.send_keys(Keys.RETURN)

        # 1 ru
        assert self.is_element_present(*NewsPageLocators.LANGUAGE_CHOOSE_1), "chose-language area is not presented"
        lang_select = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_1)
        lang_select.click()
        ru_lang = self.browser.find_element(*NewsPageLocators.LANG1)
        ru_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_1), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_1)
        title_area.send_keys(TextFields.title_ru)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_1), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_1)
        content_area.send_keys(TextFields.content_ru)
        time.sleep(2)

        # 2 en
        assert self.is_element_present(*NewsPageLocators.LANGUAGE_CHOOSE_2), "chose-language area is not presented"
        lang_sel = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_2)
        lang_sel.click()
        en_lang = self.browser.find_element(*NewsPageLocators.LANG2)
        en_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_2), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_2)
        title_area.send_keys(TextFields.title_en)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_2), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_2)
        content_area.send_keys(TextFields.content_en)
        time.sleep(2)

        # 3 es
        lang_sel = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_2)
        lang_sel.click()
        de_lang = self.browser.find_element(*NewsPageLocators.LANG3)
        de_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_3), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_3)
        title_area.send_keys(TextFields.title_es)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_3), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_3)
        content_area.send_keys(TextFields.content_es)
        time.sleep(2)

        # 4 de
        lang_sel = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_2)
        lang_sel.click()
        de_lang = self.browser.find_element(*NewsPageLocators.LANG4)
        de_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_4), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_4)
        title_area.send_keys(TextFields.title_de)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_4), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_4)
        content_area.send_keys(TextFields.content_de)
        time.sleep(2)

        assert self.is_element_present(*NewsPageLocators.SOURSE_LINK), "LINK area is not presented"
        link_area = self.browser.find_element(*NewsPageLocators.SOURSE_LINK)
        link_area.send_keys("https://strikeapi2.herokuapp.com/")
        time.sleep(2)

        assert self.is_element_present(*NewsPageLocators.TAG), "Tag area is not presented"
        tag_area = self.browser.find_element(*NewsPageLocators.TAG)
        tag_area.send_keys("Lorem")
        tag_area.send_keys(Keys.RETURN)
        tag_area.send_keys("Ipsum")
        tag_area.send_keys(Keys.RETURN)
        time.sleep(3)

        assert self.is_element_present(*NewsPageLocators.PHOTO_URL), "photo area is not presented"
        photo = self.browser.find_element(*NewsPageLocators.PHOTO_URL)
        photo.send_keys("http://www.xa-xa.org/uploads/posts/2009-05/1241337560_238965_235963.jpg")
        photo.send_keys(Keys.RETURN)
        time.sleep(2)

        assert self.is_element_present(*NewsPageLocators.CHECKBOX), "checkbox is not presented"
        tag_area = self.browser.find_element(*NewsPageLocators.CHECKBOX)
        self.browser.execute_script('return arguments[0].scrollIntoView (true);', tag_area)
        tag_area.click()
        time.sleep(3)

        assert self.is_element_present(*NewsPageLocators.CREATE_NEWS_BUTTON), "create button is not presented"

        create_news = self.browser.find_element(*NewsPageLocators.CREATE_NEWS_BUTTON)
        self.browser.execute_script('return arguments[0].scrollIntoView (true);', create_news)
        create_news.click()
        time.sleep(5)



        #cansel from create page
    # assert self.is_element_present(*NewsPageLocators.CANCEL_BUTTON), "cancel-button is not presented"
    # btn_cancel = self.browser.find_element(*NewsPageLocators.CANCEL_BUTTON)
    # btn_cancel.click()
    # time.sleep(3)
