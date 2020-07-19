from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class CheckBoxPage(BasePage):

    url = 'https://demoqa.com/checkbox'


    @property
    def check_box_button(self):
        locator = Locator(By.XPATH, '//span[text()="Check Box"]/..')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def home_check_box(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="rct-checkbox"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def success_text(self):
        locator = Locator(By.XPATH, '//span[text()="You have selected :"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def expand_all_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[title="Expand all"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def collapse_all(self):
        locator = Locator(By.CSS_SELECTOR, 'button[aria-label="Collapse all"]')
        return BaseElement(driver=self.driver, locator=locator)