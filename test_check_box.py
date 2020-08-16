from pages.check_box_page import CheckBoxPage
from pages.drivers import Drivers

browser = Drivers('--start-maximized').chrome()
cbp = CheckBoxPage(driver=browser)

sc_text = 'You have selected :'

# test start
cbp.go()
cbp.check_box_button.click()
cbp.home_check_box.click()
assert cbp.success_text.text == sc_text
cbp.expand_all_button.click()
cbp.collapse_all.click()
browser.quit()
