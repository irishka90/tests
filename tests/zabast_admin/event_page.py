import time

from selenium.webdriver.common.keys import Keys

from tests.zabast_admin.base_page import BasePage
from tests.zabast_admin.locators import NewsPageLocators, BasePageLocators, EventPageLocators


class EventPage(BasePage):
    def go_to_event_page(self):
        assert self.is_element_present(*BasePageLocators.EVENT), "Event is not presented"
        event = self.browser.find_element(*BasePageLocators.EVENT)
        event.click()
        time.sleep(3)
        assert self.browser.current_url == "https://dev.zabastcom.org/moderation/#/events", "impossible to go to event page"

    def create_button(self):
        assert self.is_element_present(*EventPageLocators.CREATE_BUTTON), "Create-button is not presented"
        button_submit = self.browser.find_element(*EventPageLocators.CREATE_BUTTON)
        button_submit.click()
        time.sleep(3)

    def create_event(self):
       # time.sleep(2000)

        assert self.is_element_present(*EventPageLocators.TYPE_EVENT), "type-event area is not presented"
        type_ev = self.browser.find_element(*EventPageLocators.TYPE_EVENT)
        type_ev.click()
        choose_type_ev = self.browser.find_element(*EventPageLocators.TYPE_EVENT_1)
        choose_type_ev.click()
        time.sleep(2)

        assert self.is_element_present(*EventPageLocators.COUNTRY_CHOOSE), "country area is not presented"
        country = self.browser.find_element(*EventPageLocators.COUNTRY_CHOOSE)
        country.click()
        choose_country = self.browser.find_element(*EventPageLocators.TYPE_EVENT_1)
        choose_country.click()
        time.sleep(2)

        assert self.is_element_present(*EventPageLocators.REGION), "region area is not presented"
        reg = self.browser.find_element(*EventPageLocators.REGION)
        reg.click()
        reg.send_keys("смо")
        reg_choose = self.browser.find_element(*EventPageLocators.REGION_CHOOSE)
        reg_choose.click()

      #  assert self.is_element_present(*EventPageLocators.TOWN), "Town area is not presented"
      #  town = self.browser.find_element(*EventPageLocators.TOWN)
      #  town.send_keys("рудня")
       # town.send_keys(Keys.RETURN)




