from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class TextBoxPage(BasePage):

    url = 'https://demoqa.com/text-box'

    @property
    def text_box_button(self):
        locator = Locator(By.XPATH, '(//li[@id="item-0"])[1]')
        return BaseElement(driver=self.driver,locator=locator)

    @property
    def full_name_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="userName"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="userEmail"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def address1_input(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def address2_input(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sab_name(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_email(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="email"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_address1(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="currentAddress"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sub_address2(self):
        locator = Locator(By.CSS_SELECTOR, 'p[id="permanentAddress"]')
        return BaseElement(driver=self.driver, locator=locator)