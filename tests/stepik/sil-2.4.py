from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id("book")
butn1 = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button.click()

num = browser.find_element_by_id("input_value")
x = num.text
y = calc(int(x))

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

butn2 = browser.find_element_by_id("solve")
butn2.click()
