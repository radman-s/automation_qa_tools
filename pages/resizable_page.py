from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class ResizablePage(BasePage):

    url = 'https://demoqa.com/resizable'

    @property
    def box1(self):
        locator = Locator(By.XPATH, '(//span[@class="react-resizable-handle react-resizable-handle-se"])[1]')
        return BaseElement(driver=self.driver, locator=locator)





