from selenium.webdriver.common.by import By

from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class DroppablePage(BasePage):

    url = 'https://demoqa.com/droppable'

    # SIMPLE
    @property
    def drag_me(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="draggable"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def simple_drop_here(self):
        element = self.driver.find_element_by_xpath('(//div[@id="droppable"])[1]')
        return element

    # ACCEPT
    @property
    def ac_tab(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def ac_drop(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="acceptable"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def no_ac_drop(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="notAcceptable"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def ac_drop_here(self):
        element = self.driver.find_element_by_xpath('(//div[@id="droppable"])[2]')
        return element




