from selenium import webdriver
from pages.slider_page import SliderPage

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

sp = SliderPage(driver=browser)

sp.go()
sp.slider.drag(30, 0)
sp.slider.drag(0, 40)
sp.slider.drag(60, 0)
browser.quit()



