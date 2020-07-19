from selenium import webdriver
from pages.resizable_page import ResizablePage

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)
rp = ResizablePage(driver=browser)

rp.go()
rp.box1.drag(-50, -50)
rp.box1.drag(350, 0)
rp.box1.drag(-350, 150)
rp.box1.drag(350, 0)
rp.box1.drag(-300, -100)
browser.quit()























