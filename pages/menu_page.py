from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class MenuPage(BasePage):

    url = 'https://demoqa.com/menu#'


    @property
    def main_item1(self):
        locator = Locator(By.XPATH, '//a[text()="Main Item 1"]/..')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_item2(self):
        locator = Locator(By.XPATH, '//a[text()="Main Item 2"]/..')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_item3(self):
        locator = Locator(By.XPATH, '//a[text()="Main Item 3"]/..')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_item1(self):
        locator = Locator(By.XPATH, '(//a[text()="Sub Item"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_item2(self):
        locator = Locator(By.XPATH, '(//a[text()="Sub Item"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_sub_list(self):
        locator = Locator(By.XPATH, '//a[text()="SUB SUB LIST »"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_sub_item1(self):
        locator = Locator(By.XPATH, '//a[text()="Sub Sub Item 1"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_sub_item2(self):
        locator = Locator(By.XPATH, '//a[text()="Sub Sub Item 2"]')
        return BaseElement(driver=self.driver, locator=locator)




