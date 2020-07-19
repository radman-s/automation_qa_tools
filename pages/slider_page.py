from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class SliderPage(BasePage):

    url = 'https://demoqa.com/slider'

    @property
    def slider(self):
        locator = Locator(By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
        return BaseElement(driver=self.driver, locator=locator)




