# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

from pages.BasePage import BasePage
from pages.searchbox_calendar import SearchBoxCalendar
from locators import SearchBoxLocators


class InsuranceSearchBox(BasePage):

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SearchBoxLocators.SEARCH_BUTTON))

        search_button.click()

    def set_destination(self, typeof, country):
        if typeof == "arrival":
            arrival_destination = Select(self.driver.find_element_by_id(SearchBoxLocators.ARRIVAL_COUNTRY))
            arrival_destination.select_by_visible_text(country)
        elif typeof == "departure":
            departure_destination = Select(self.driver.find_element_by_id(SearchBoxLocators.DEPARTURE_COUNTRY))
            departure_destination.select_by_visible_text(country)
        else:
            print("only arrival or departure Type is allowed")

    def set_date(self, typeof, month_year, day):

        if typeof == "start":
            calendar_box = self.driver.find_element_by_id(SearchBoxLocators.START_DATE)
            calendar_box.click()
            calendar = SearchBoxCalendar(self.driver)
            calendar.set_date(month_year, day)
        elif typeof == "end":
            calendar_box = self.driver.find_element_by_id(SearchBoxLocators.END_DATE)
            calendar_box.click()
            calendar = SearchBoxCalendar(self.driver)
            calendar.set_date(month_year, day)

        else:
            print("only start or end Type is allowed")

    def get_price_info(self):
        validate_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SearchBoxLocators.INSURANCE_VALUE)))
        return validate_msg.text










