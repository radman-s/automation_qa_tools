from pages.tooltips_page import TooltipsPage
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

tp = TooltipsPage(driver=browser)

tp.go()
tp.hover_button.move_to()
tp.hover_input.move_to()
tp.hover_link_contary.move_to()
tp.hover_link_number.move_to()
browser.quit()












