from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class TooltipsPage(BasePage):

    url = 'https://demoqa.com/tool-tips'

    @property
    def hover_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="toolTipButton"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hover_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hover_link_contary(self):
        locator = Locator(By.XPATH, '//a[text()="Contrary"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hover_link_number(self):
        locator = Locator(By.XPATH, '//a[text()="1.10.32"]')
        return BaseElement(driver=self.driver, locator=locator)





