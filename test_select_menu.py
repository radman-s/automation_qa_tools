from pages.drivers import Drivers
from pages.select_menu_page import SelectMenuPage

browser = Drivers('--start-maximized').chrome()
smp = SelectMenuPage(driver=browser)

# test start
smp.go()
# SELECT OPTIONS
# hover
smp.select_value.click()
smp.g1_option2.move_to()
smp.g1_option2.move_to()
smp.g2_option1.move_to()
smp.g2_option2.move_to()
smp.r_option.move_to()
smp.a_r_option.move_to()

# select
smp.a_r_option.click()

smp.select_value.click()
smp.r_option.click()

smp.select_value.click()
smp.g2_option2.click()

smp.select_value.click()
smp.g2_option1.click()

smp.select_value.click()
smp.g1_option2.click()

smp.select_value.click()
smp.g1_option1.click()

# SELECT ONE
# hover
smp.select_one.click()
smp.dr.move_to()
smp.mr.move_to()
smp.mrs.move_to()
smp.ms.move_to()
smp.prof.move_to()
smp.other.move_to()

# select
smp.other.click()

smp.select_one.click()
smp.prof.click()

smp.select_one.click()
smp.ms.click()

smp.select_one.click()
smp.mrs.click()

smp.select_one.click()
smp.mr.click()

smp.select_one.click()
smp.dr.click()

# OLD STYLE SELECT MENU
smp.old_style_menu.select_drop('10')
smp.old_style_menu.select_drop('9')
smp.old_style_menu.select_drop('8')
smp.old_style_menu.select_drop('7')
smp.old_style_menu.select_drop('6')
smp.old_style_menu.select_drop('5')
smp.old_style_menu.select_drop('4')
smp.old_style_menu.select_drop('3')
smp.old_style_menu.select_drop('2')
smp.old_style_menu.select_drop('1')
smp.old_style_menu.select_drop('red')
browser.quit()
print('test passed')













