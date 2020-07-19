from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class DatePickerPage(BasePage):

    url = 'https://demoqa.com/date-picker'

    # SELECT DATE
    @property
    def date_input1(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def month_drop1(self):
        locator = Locator(By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def year_drop1(self):
        locator = Locator(By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def date_30_1(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="react-datepicker__day react-datepicker__day--030"]')
        return BaseElement(driver=self.driver, locator=locator)


    # DATE AND TIME
    @property
    def date_input2(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def time_select(self):
        locator = Locator(By.XPATH, '//li[text()="07:45"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def month_drop2(self):
        locator = Locator(By.XPATH, '//span[text()="July"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def year_drop2(self):
        locator = Locator(By.XPATH, '//div[text()="2020"]')
        return BaseElement(driver=self.driver, locator=locator)














