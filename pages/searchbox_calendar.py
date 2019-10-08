# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

from locators import SearchBoxCalendarLocators
from pages.BasePage import BasePage


class SearchBoxCalendar(BasePage):

    def set_date(self, month_year, day):
        month = self.driver.find_element_by_xpath(SearchBoxCalendarLocators.TITLE_DATE).text
        while month not in month_year:
            month = self.driver.find_element_by_xpath(SearchBoxCalendarLocators.TITLE_DATE).text
            next_month = self.driver.find_element_by_xpath(SearchBoxCalendarLocators.NEXT_MONTH)
            if month != month_year:
                next_month.click()
        day = self.driver.find_element_by_xpath("//a[@class='ui-state-default' and contains(text()," + day + ")]")
        day.click()
        time.sleep(4)
