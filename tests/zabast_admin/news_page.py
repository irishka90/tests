import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.zabast_admin.dashboard_page import DashboardPage
from tests.zabast_admin.locators import NewsPageLocators, TextFields
from tests.zabast_admin.locators import BasePageLocators


class NewsPage(DashboardPage):

    def create_button(self):
        first_id_on_page = self.browser.find_element_by_class_name("baseTable__body") \
            .find_elements_by_class_name("baseTable__row")[0] \
            .find_elements_by_class_name("baseTable__cell")[0].text
        assert self.is_element_present(*NewsPageLocators.CREATE_BUTTON), "Create-button is not presented"
        button_submit = self.browser.find_element(*NewsPageLocators.CREATE_BUTTON)
        button_submit.click()
        time.sleep(3)

    #   assert  self.is_element_present(*NewsPageLocators.CHOOSE_DATE), "impossible to go to create_news window"

    def create_news(self):
        assert self.is_element_present(*NewsPageLocators.CHOOSE_DATE), "chose-date area is not presented"
        date_area = self.browser.find_element(*NewsPageLocators.CHOOSE_DATE)
        save_date = TextFields.date
        date_area.send_keys(save_date)
        date_area.send_keys(Keys.RETURN)

        assert self.is_element_present(*NewsPageLocators.PHOTO_URL), "photo area is not presented"
        photo = self.browser.find_element(*NewsPageLocators.PHOTO_URL)
        photo.send_keys(TextFields.image)
        photo.send_keys(Keys.RETURN)
        photo.send_keys(TextFields.image2)
        photo.send_keys(Keys.RETURN)
        time.sleep(5)

        """assert self.is_element_present(*NewsPageLocators.VIDEO_ADD), "Button 'add video'not presented"
        add_video = self.browser.find_element(*NewsPageLocators.VIDEO_ADD)
        add_video.click()
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.VIDEO_ADD_WINDOW), "Add video window not presented"
        assert self.is_element_present(*NewsPageLocators.ADD_URL), "Add video url not presented"
        add_url = self.browser.find_element(*NewsPageLocators.ADD_URL)
        add_url.send_keys(TextFields.video_url)
        time.sleep(5)
        assert self.is_element_present(*NewsPageLocators.VIDEO_TYPE), "type selector not presented"
        video_type = self.browser.find_element(*NewsPageLocators.VIDEO_TYPE)
        video_type.click()
        youtube = self.browser.find_element(*NewsPageLocators.YOUTUBE)
        youtube.click()
        add_button = self.browser.find_element(*NewsPageLocators.VIDEO_ADD_BUTTON)
        add_button.click()"""

        # 1 ru
        assert self.is_element_present(*NewsPageLocators.LANGUAGE_CHOOSE_1), "chose-language area is not presented"
        lang_select = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_1)
        lang_select.click()
        ru_lang = self.browser.find_element(*NewsPageLocators.LANG1)
        ru_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_1), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_1)
        ru_title = TextFields.title_ru
        title_area.send_keys(ru_title)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_1), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_1)
        ru_content = TextFields.content_ru
        content_area.send_keys(ru_content)
        time.sleep(2)

        # 2 en
        assert self.is_element_present(*NewsPageLocators.LANGUAGE_CHOOSE_2), "chose-language area is not presented"
        lang_sel = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_2)
        lang_sel.click()
        en_lang = self.browser.find_element(*NewsPageLocators.LANG2)
        en_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_2), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_2)
        en_title = TextFields.title_en
        title_area.send_keys(en_title)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_2), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_2)
        en_content = TextFields.content_en
        content_area.send_keys(en_content)
        time.sleep(2)

        # 3 es
        lang_sel = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_2)
        lang_sel.click()
        de_lang = self.browser.find_element(*NewsPageLocators.LANG3)
        de_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_3), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_3)
        es_title = TextFields.title_es
        title_area.send_keys(es_title)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_3), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_3)
        es_content = TextFields.content_es
        content_area.send_keys(es_content)
        time.sleep(2)

        # 4 de
        lang_sel = self.browser.find_element(*NewsPageLocators.LANGUAGE_CHOOSE_2)
        lang_sel.click()
        de_lang = self.browser.find_element(*NewsPageLocators.LANG4)
        de_lang.click()
        assert self.is_element_present(*NewsPageLocators.TITLE_4), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_4)
        de_title = TextFields.title_de
        title_area.send_keys(de_title)
        time.sleep(2)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_4), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_4)
        de_content = TextFields.content_de
        content_area.send_keys(de_content)
        time.sleep(2)

        assert self.is_element_present(*NewsPageLocators.SOURSE_LINK), "LINK area is not presented"
        link_area = self.browser.find_element(*NewsPageLocators.SOURSE_LINK)
        link_news = TextFields.url_source
        link_area.send_keys(link_news)
        time.sleep(2)

        assert self.is_element_present(*NewsPageLocators.TAG), "Tag area is not presented"
        tag_area = self.browser.find_element(*NewsPageLocators.TAG)
        tag1 = TextFields.tag_1
        tag_area.send_keys(tag1)
        tag_area.send_keys(Keys.RETURN)
        tag2 = TextFields.tag_2
        tag_area.send_keys(tag2)
        tag_area.send_keys(Keys.RETURN)
        time.sleep(3)

        # assert self.is_element_present(*NewsPageLocators.CHECKBOX), "checkbox is not presented"
        #  tag_area = self.browser.find_element(*NewsPageLocators.CHECKBOX)
        #  self.browser.execute_script('return arguments[0].scrollIntoView (true);', tag_area)
        # tag_area.click()
        #  time.sleep(3)

        assert self.is_element_present(*NewsPageLocators.CREATE_NEWS_BUTTON), "create button is not presented"
        create_news = self.browser.find_element(*NewsPageLocators.CREATE_NEWS_BUTTON)
        self.browser.execute_script('return arguments[0].scrollIntoView (true);', create_news)
        create_news.click()
        time.sleep(5)
        table = \
            self.browser.find_element_by_class_name("baseTable__body").find_elements_by_class_name("baseTable__row")[
                0].find_elements_by_class_name("baseTable__cell")[2].find_element_by_tag_name("span").text

        print("date in table", table)
        print("date news", save_date)
        assert save_date in table, "not equal date"

        # Открываем созданую новость на редактирование и проверяем соответствие отображаемых полей введенным ранее
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
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_1).get_attribute('value')
        assert title_area == ru_title, "Not equal ru_titles 1{} 2{}".format(title_area, ru_title)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_1), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_1).get_attribute('value')
        assert content_area == ru_content, "Not equal ru_content 1{} 2{}".format(content_area, ru_content)

        assert self.is_element_present(*NewsPageLocators.TITLE_1), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_2).get_attribute('value')
        assert title_area == en_title, "Not equal en_titles 1{} 2{}".format(title_area, en_title)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_2), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_2).get_attribute('value')
        assert content_area == en_content, "Not equal en_content 1{} 2{}".format(content_area, en_content)

        assert self.is_element_present(*NewsPageLocators.TITLE_3), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_3).get_attribute('value')
        assert title_area == es_title, "Not equal es_titles 1{} 2{}".format(title_area, es_title)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_3), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_3).get_attribute('value')
        assert content_area == es_content, "Not equal es_content 1{} 2{}".format(content_area, es_content)

        assert self.is_element_present(*NewsPageLocators.TITLE_4), "Title area is not presented"
        title_area = self.browser.find_element(*NewsPageLocators.TITLE_4).get_attribute('value')
        assert title_area == de_title, "Not equal de_titles 1{} 2{}".format(title_area, de_title)
        assert self.is_element_present(*NewsPageLocators.DESCRIPTION_4), "Content area is not presented"
        content_area = self.browser.find_element(*NewsPageLocators.DESCRIPTION_4).get_attribute('value')
        assert content_area == de_content, "Not equal de_content 1{} 2{}".format(content_area, de_content)

        # Проверка ссылки
        assert self.is_element_present(*NewsPageLocators.SOURSE_LINK), "LINK area is not presented"
        link_area = self.browser.find_element(*NewsPageLocators.SOURSE_LINK).get_attribute('value')
        assert link_area == link_news, "Not equal links 1{} 2{}".format(link_area, link_news)

        # Проверка тэга
        """assert self.is_element_present(*NewsPageLocators.TAG), "Tag area is not presented"
        tag_area1 = self.browser.find_element(*NewsPageLocators.TAG).find_element(By.XPATH,
                                                                                  "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[7]/div/div/span[1]/span").text
        tag_area2 = self.browser.find_element(*NewsPageLocators.TAG).find_element(By.XPATH,
                                                                                  "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[7]/div/div/span[2]/span").text
        assert tag_area1 + tag_area2 == tag1 + tag2, "Not equal tags 1{} 2{}".format(tag_area, tag1 + tag2)

    # cansel from create page
    # assert self.is_element_present(*NewsPageLocators.CANCEL_BUTTON), "cancel-button is not presented"
    # btn_cancel = self.browser.find_element(*NewsPageLocators.CANCEL_BUTTON)
    # btn_cancel.click()
    # time.sleep(3)"""

