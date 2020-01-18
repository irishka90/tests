import time
from selenium.common.exceptions import NoSuchElementException
from tests.zabast_admin.locators import BasePageLocators

link = "http://104.248.35.86/moderation/#/login"


class BasePage():

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://104.248.35.86/moderation", \
            "link is not correct "

    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not presented"
        time.sleep(7)

    def log_out(self):
        assert self.is_element_present(*BasePageLocators.LOG_OUT), "Log-out button not found"
        get_out = self.browser.find_element(*BasePageLocators.LOG_OUT)
        get_out.click()
        out_button = self.browser.find_element(*BasePageLocators.OUT_BUTTON)
        out_button.click()
        time.sleep(3)

    def change_page(self):
        assert self.is_element_present(*BasePageLocators.FORWARD_BUTTON), "Forward button not found"
        one_page_forward = self.browser.find_element(*BasePageLocators.FORWARD_BUTTON)
        one_page_forward.click()
        assert self.is_element_present(*BasePageLocators.BACK_BUTTON), "Back button not found"
        one_page_back = self.browser.find_element(*BasePageLocators.BACK_BUTTON)
        one_page_back.click()
        assert self.is_element_present(*BasePageLocators.CHOOSE_PAGE_3), "page 3 button not found"
        one_page_back = self.browser.find_element(*BasePageLocators.CHOOSE_PAGE_3)
        one_page_back.click()




    def get_in(self, email="admin_tester@gmail.com", password="q1w2e3r4"):
        assert self.is_element_present(*BasePageLocators.LOGIN_INPUT), "Not found email input"
        email_input = self.browser.find_element(*BasePageLocators.LOGIN_INPUT)
        email_input.send_keys(email)
        assert self.is_element_present(*BasePageLocators.PASSWORD_INPUT), "Not found password1 input"
        password_1 = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_1.send_keys(password)
        assert self.is_element_present(*BasePageLocators.REG_SUBMIT), "Not found button registration"
        button_submit = self.browser.find_element(*BasePageLocators.REG_SUBMIT)
        button_submit.click()
        time.sleep(7)
