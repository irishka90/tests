import time
import pytest


link = "https://strikeapi.herokuapp.com"

class TestZabast():
    @pytest.mark.xfail
    def test_news(self, browser, open_main, base_tab_news):
        tab = browser.find_element_by_class_name("headerNavItem__text")
        time.sleep(5)
        assert base_tab_news == tab, "Нет"

    @pytest.mark.xfail
    def test_news_read(self, browser, open_main, base_tab_news):
        read_news = browser.find_element_by_id("item-385")
        header_text_1 = browser.find_element_by_xpath(
            "/html/body/div/section/main/div/div/div/div[2]/div[1]/div/h2").text
        read_news.click()
        time.sleep(3)
        header_text_2 = browser.find_element_by_xpath("/html/body/div/section/main/div/div/div[1]/h2").text
        assert header_text_1 == header_text_2, "не та новость"

    @pytest.mark.xfail
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

    @pytest.mark.xfail
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
        button = browser.find_element_by_class_name("el-button--primary")
        button.click()
        time.sleep(5)
        #assert

    @pytest.mark.xfail
    def test_map_view(self, browser, open_main, registration_with_login):
        map = browser.find_element_by_xpath("/html/body/div/section/header/div/div[2]/ul/li[3]")
        map.click()
        time.sleep(5)
        return map
