import pytest
from selenium import webdriver
import time
import math



@pytest.mark.parametrize('link_part',
                         ["236895", "236896", "236897", "236898", "236899", "236903",
                          "236904", "236905"])
def test_3_6(browser, link_part):
    link = f"https://stepik.org/lesson/{link_part}/step/1/"
    browser.get(link)
    time.sleep(3)
    y = str(math.log(int(time.time())))
    time.sleep(3)
    answer = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/div/div[3]/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/textarea")
    answer.send_keys(y)
    time.sleep(5)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(3)
    result=browser.find_element_by_class_name("smart-hints__hint").text

    assert result=="Correct!", "не выполнен"

