from pages.buttons_page import ButtonsPage
from pages.drivers import Drivers

browser = Drivers('--start-maximized').chrome()
bp = ButtonsPage(driver=browser)

# test start
bp.go()
bp.buttons_button.click()
bp.double_click_button.double_click()
assert bp.double_click_msg.text == 'You have done a double click'
bp.right_click_button.right_click()
assert bp.right_click_msg.text == 'You have done a right click'
click_me_button = browser.find_element_by_xpath('//button[text()="Click Me"]')
click_me_button.click()
assert bp.click_me_msg.text == 'You have done a dynamic click'
browser.quit()
print('test passed')