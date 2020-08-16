from pages.drivers import Drivers
from pages.menu_page import MenuPage

browser = Drivers('--start-maximized').chrome()
mp = MenuPage(driver=browser)

# test start
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
print('test passed')




















