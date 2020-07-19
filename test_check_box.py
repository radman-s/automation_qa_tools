from pages.check_box_page import CheckBoxPage
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

cbp = CheckBoxPage(driver=browser)

sc_text = 'You have selected :'

cbp.go()
cbp.check_box_button.click()
cbp.home_check_box.click()
assert cbp.success_text.text == sc_text
cbp.expand_all_button.click()
cbp.collapse_all.click()
browser.quit()
