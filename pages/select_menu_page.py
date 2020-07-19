from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class SelectMenuPage(BasePage):

    url = 'https://demoqa.com/select-menu'

    # SELECT VALUE
    @property
    def select_value(self):
        locator = Locator(By.XPATH, '(//div[@class=" css-1hwfws3"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g1_option1(self):
        locator = Locator(By.XPATH, '//div[text()="Group 1, option 1"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g1_option2(self):
        locator = Locator(By.XPATH, '//div[text()="Group 1, option 2"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g2_option1(self):
        locator = Locator(By.XPATH, '//div[text()="Group 2, option 1"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g2_option2(self):
        locator = Locator(By.XPATH, '//div[text()="Group 2, option 2"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def a_r_option(self):
        locator = Locator(By.XPATH, '//div[text()="Another root option"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def r_option(self):
        locator = Locator(By.XPATH, '//div[text()="A root option"]')
        return BaseElement(driver=self.driver, locator=locator)


    # SELECT ONE
    @property
    def select_one(self):
        locator = Locator(By.XPATH, '(//div[@class=" css-1hwfws3"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def dr(self):
        locator = Locator(By.XPATH, '//div[text()="Dr."]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def mr(self):
        locator = Locator(By.XPATH, '//div[text()="Mr."]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def mrs(self):
        locator = Locator(By.XPATH, '//div[text()="Mrs."]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def ms(self):
        locator = Locator(By.XPATH, '//div[text()="Ms."]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def prof(self):
        locator = Locator(By.XPATH, '//div[text()="Prof."]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def other(self):
        locator = Locator(By.XPATH, '//div[text()="Other"]')
        return BaseElement(driver=self.driver, locator=locator)

    # OLD STYLE SELECT MENU
    @property
    def old_style_menu(self):
        locator = Locator(By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')
        return BaseElement(driver=self.driver, locator=locator)


