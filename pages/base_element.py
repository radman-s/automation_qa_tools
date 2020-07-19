from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()


    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def click_nw(self):
        self.web_element.click()
        return None

    def double_click(self):
        element = ActionChains(self.driver)
        element.double_click(self.web_element).perform()
        return None

    def right_click(self):
        element = ActionChains(self.driver)
        element.context_click(self.web_element).perform()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def select_drop(self, val):
        element = Select(self.web_element)
        element.select_by_value(val)
        return None

    def drag(self, offset, yoffset):
        element = ActionChains(self.driver)
        element.click_and_hold(self.web_element).move_by_offset(offset, yoffset).release().perform()
        return None

    def move_to(self):
        element = ActionChains(self.driver)
        element.move_to_element(self.web_element).perform()
        return None

    def drag_drop(self, target):
        element = ActionChains(self.driver)
        element.click_and_hold(self.web_element).move_to_element(self.web_element).release(target).perform()
        return None





































