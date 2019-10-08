# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from pages.insurance_searchbox import InsuranceSearchBox


class SearchInsurance(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.esky.pl/ubezpieczenie-podrozne")

    def tearDown(self):

        self.driver.quit()

    def test_validate_insurance_price_info_main_page(self):
        search_box = InsuranceSearchBox(self.driver)
        search_box.set_destination("departure", "Niemcy")
        search_box.set_destination("arrival", "Polska")
        search_box.set_date("start", "Styczeń 2020", "11")
        search_box.set_date("end", "Styczeń 2020", "22")
        self.assertIn(search_box.get_price_info(), 'Cena ubezpieczenia:')


if __name__ == '__main__':
    unittest.main(verbosity=2)