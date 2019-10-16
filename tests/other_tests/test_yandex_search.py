import time
import unittest


from selenium import webdriver




class TestSearch(unittest.TestCase):
    def test_search_yandex(self):
        link = "https://yandex.by/"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_class_name("input__control.input__input")
        input1.send_keys("car")

        button = browser.find_element_by_class_name('search2__button')
        button.click()

        time.sleep(5)

        element = browser.find_element_by_partial_link_text("4you - новые автомобили в лизинг с расчетом...")
        element.click()

        time.sleep(15)
if __name__ == "__main__":
    unittest.main()
