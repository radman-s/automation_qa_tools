from pages.drivers import Drivers
from pages.slider_page import SliderPage

browser = Drivers('--start-maximized').chrome()
sp = SliderPage(driver=browser)

# test start
sp.go()
sp.slider.drag(30, 0)
sp.slider.drag(0, 40)
sp.slider.drag(60, 0)
browser.quit()
print('test passed')



