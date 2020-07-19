from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class ButtonsPage(BasePage):

    url = 'https://demoqa.com/buttons'

    @property
    def buttons_button(self):
        locator = Locator(By.XPATH, '//span[text()="Buttons"]/..')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def double_click_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def double_click_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def right_click_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def right_click_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_me_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="6Zq5d"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_me_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')
        return BaseElement(driver=self.driver, locator=locator)