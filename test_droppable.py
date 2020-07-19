from selenium import webdriver
from pages.droppable_page import DroppablePage

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

dp = DroppablePage(driver=browser)

dp.go()

# SIMPLE
dp.drag_me.drag_drop(dp.simple_drop_here)

# ACCEPT
dp.ac_tab.click()
dp.no_ac_drop.drag_drop(dp.ac_drop_here)
dp.no_ac_drop.drag(-200, 50)
dp.ac_drop.drag_drop(dp.ac_drop_here)
browser.quit()
















