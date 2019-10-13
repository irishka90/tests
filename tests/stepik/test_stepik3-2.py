import time
import unittest

from selenium import webdriver


def base_reg(self, link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("first_block").find_element_by_class_name(
        "form-group.first_class").find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("first_block").find_element_by_class_name(
        "form-group.second_class").find_element_by_tag_name("input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("first_block").find_element_by_class_name(
        "form-group.third_class").find_element_by_tag_name("input")
    input3.send_keys("a@Smol.ensk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    browser.quit()


class TestNum(unittest.TestCase):

    def test_reg(self):
        base_reg(self, "http://suninjuly.github.io/registration1.html")

    def test_reg2(self):
        base_reg(self, "http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
