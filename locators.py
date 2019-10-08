from selenium.webdriver.common.by import By


class SearchBoxLocators(object):

    SEARCH_BUTTON = "//button[@class='btn transaction qsf-search']"

    ARRIVAL_COUNTRY = "arrivalCountry"

    DEPARTURE_COUNTRY = "departureCountry"

    EMPTY_FIELD_MSGS = "//em[@class='error-msg']"

    START_DATE = "startDate"

    END_DATE = "endDate"

    PAX = (By.XPATH, "//div[@data-content-id='pax-counter-insurance']")

    INSURANCE_VALUE = "//div[@class='label']"


class SearchBoxCalendarLocators(object):

    MONTH = "ui-datepicker-month"

    YEAR = "ui-datepicker-year"

    NEXT_MONTH = "//a[@data-handler='next']"

    PREV_MONTH = "//a[@data-handler='prev']"

    TITLE_DATE = "//div[@class='ui-datepicker-title']"

