from selenium import webdriver
from pages.menu_page import MenuPage

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

mp = MenuPage(driver=browser)

mp.go()
mp.main_item2.move_to()
mp.sub_item1.move_to()
mp.sub_item2.move_to()
mp.sub_sub_list.move_to()
mp.sub_sub_item1.move_to()
mp.sub_sub_item2.move_to()
mp.main_item3.move_to()
mp.main_item1.move_to()
browser.quit()




















