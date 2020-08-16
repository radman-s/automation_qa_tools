from pages.drivers import Drivers
from pages.resizable_page import ResizablePage

browser = Drivers('--start-maximized').chrome()
rp = ResizablePage(driver=browser)

# test start
rp.go()
rp.box1.drag(-50, -50)
rp.box1.drag(350, 0)
rp.box1.drag(-350, 150)
rp.box1.drag(350, 0)
rp.box1.drag(-300, -100)
browser.quit()
print('test passed')






















