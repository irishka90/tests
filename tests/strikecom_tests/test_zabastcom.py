import time
import unittest
from selenium import webdriver


class TestZabast(unittest.TestCase):
    def test_news(self):
        link = "https://strikeapi.herokuapp.com"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)

        # news=browser.find_elements_by_class_name("el-menu-item.headerNav__item.is-active")[0]
        news = browser.find_element_by_xpath("/html/body/div/section/header/div/div[2]/ul/li[2]/span")
        news.click()
        time.sleep(3)

        #read_news = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div[5]/div[1]")
        read_news = browser.find_element_by_id("item-385")
        header_text_1 = browser.find_element_by_xpath(
            "/html/body/div/section/main/div/div/div/div[2]/div[1]/div/h2").text
        read_news.click()
        time.sleep(5)


        header_text_2 = browser.find_element_by_xpath("/html/body/div/section/main/div/div/div[1]/h2").text
        print(header_text_1, header_text_2)
        self.assertEqual(header_text_2, header_text_1, "заголовки разные")

    def test_entrance(self):
        link = "https://strikeapi.herokuapp.com"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(2)

        button= browser.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/ul/div/button")
        button.click()
        time.sleep(2)

        input_1 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[3]/input")
        input_1.send_keys("test@test.test")
        input_2 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[4]/input")
        input_2.send_keys("qwe123")
        button = browser.find_element_by_class_name("el-button.authSectionDialogForm__button.el-button--primary")
        button.click()
        time.sleep(2)

    def test_comment(self):
        link = "https://strikeapi.herokuapp.com"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(2)

        button = browser.find_element_by_xpath("/html/body/div[1]/section/header/div/div[2]/ul/div/button")
        button.click()
        time.sleep(2)

        input_1 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[3]/input")
        input_1.send_keys("test@test.test")
        input_2 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[4]/input")
        input_2.send_keys("qwe123")
        button = browser.find_element_by_class_name("el-button.authSectionDialogForm__button.el-button--primary")
        button.click()
        time.sleep(2)

        news = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div[1]/div[1]")
        news.click()
        time.sleep(3)

        browser.execute_script("window.scrollBy(0,600);")

        input_comment=browser.find_element_by_class_name("el-textarea__inner")
        input_comment.send_keys("тест-проверка")
        button=browser.find_element_by_class_name("el-button.baseComments__sendButton.el-button--default.el-button--medium")
        button.click()
        time.sleep(5)


    def test_comment_delete(self):
        link = "https://strikeapi.herokuapp.com"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(2)

        button = browser.find_element_by_class_name("el-button.authSection__button.el-button--secondary")
        button.click()
        time.sleep(2)

        input_1 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[3]/input")
        input_1.send_keys("test@test.test")
        input_2 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[4]/input")
        input_2.send_keys("qwe123")
        button = browser.find_element_by_class_name("el-button.authSectionDialogForm__button.el-button--primary")
        button.click()
        time.sleep(2)

        news = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div[1]/div[1]")
        news.click()
        time.sleep(3)

        browser.execute_script("window.scrollBy(0,600);")

        delete=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/a/span")
        delete.click()
        time.sleep(3)
        #confirm=browser.switch_to.alert
        #confirm.accept()
        button=browser.find_element_by_class_name("el-button.el-button--default.el-button--small.el-button--primary")
        button.click()
        time.sleep(5)




if __name__ == "__main__":
    unittest.main()
