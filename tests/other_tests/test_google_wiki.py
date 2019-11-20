import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TestSearch(unittest.TestCase):



    def test_search_google(self):
        link = "https://www.google.com"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_class_name("gLFyf.gsfi")
        input1.send_keys("car")

        button = browser.find_element_by_class_name("FPdoLc.VlcLAe").find_element_by_class_name("gNO89b")
        button.click()

        time.sleep(2)

        element = browser.find_element_by_xpath("//div[@class='rc']/div[@class='r']/a[1]")
        if element.is_displayed():
            actions = ActionChains(browser)
            actions.move_to_element(element).click().perform()

        time.sleep(2)


def test_search_wiki(self):
    link = "https://ru.wikipedia.org"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("search")
    input1.send_keys("music")

    button = browser.find_element_by_id("searchButton")
    button.click()
    time.sleep(3)

    language = browser.find_element_by_link_text("English")
    language.click()
    time.sleep(5)


if __name__ == "__main__":
    unittest.main()
