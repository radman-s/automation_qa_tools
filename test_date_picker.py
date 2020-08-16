from pages.drivers import Drivers
from pages.date_picker_page import DatePickerPage

browser = Drivers('--start-maximized').chrome()
dpp = DatePickerPage(driver=browser)

# test start
dpp.go()

# SELECT DATE
dpp.date_input1.click()
dpp.month_drop1.select_drop('2')
dpp.year_drop1.select_drop('1987')
dpp.date_30_1.click()

# DATE AND TIME
dpp.date_input2.click()
dpp.time_select.click()
dpp.month_drop2.click()
dpp.year_drop2.click()
browser.quit()
print('test passed')
















