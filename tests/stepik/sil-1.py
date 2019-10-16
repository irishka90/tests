from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    x=num1.text
    num2= browser.find_element_by_id("num2")
    y = num2.text
    sum = str(int(x) + int(y))
    print(sum)


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
