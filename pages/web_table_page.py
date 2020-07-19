from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class WebTablePage(BasePage):

    url = 'https://demoqa.com/webtables'


    @property
    def web_tables_button(self):
        locator = Locator(By.XPATH, '//span[text()="Web Tables"]/..')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def delete_record1(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="delete-record-1"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def delete_record2(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="delete-record-2"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def delete_record3(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="delete-record-3"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def first_name_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="firstName"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_name_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="lastName"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="userEmail"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def age_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="age"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def salary_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="salary"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def department_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="department"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_table(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_table(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="searchBox"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def rows_drop(self):
        locator = Locator(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
        return BaseElement(driver=self.driver,locator=locator)

    @property
    def next_table(self):
        locator = Locator(By.XPATH, '//button[text()="Next"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def previous_table(self):
        locator = Locator(By.XPATH, '//button[text()="Previous"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def page_table(self):
        locator = Locator(By.XPATH, 'input[aria-label="jump to page"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def first_name_row(self):
        locator = Locator(By.XPATH, '//div[text()="First Name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def action_row(self):
        locator = Locator(By.XPATH, '//div[text()="Action"]')
        return BaseElement(driver=self.driver, locator=locator)