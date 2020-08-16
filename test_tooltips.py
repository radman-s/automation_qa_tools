from pages.tooltips_page import TooltipsPage
from pages.drivers import Drivers

browser = Drivers('--start-maximized').chrome()
tp = TooltipsPage(driver=browser)

# test start
tp.go()
tp.hover_button.move_to()
tp.hover_input.move_to()
tp.hover_link_contary.move_to()
tp.hover_link_number.move_to()
browser.quit()
print('test passed')











