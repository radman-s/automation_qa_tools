from pages.text_box_page import TextBoxPage
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

tbp = TextBoxPage(driver=browser)

# Test setup
name = 'Michal Johnson'
email = 'michael@gmail.com'
addr1 = 'Wilson rd.5, Prague'
addr2 = 'Czech Republic'

tbp.go()
tbp.text_box_button.click()
tbp.full_name_input.input_text(name)
tbp.email_input.input_text(email)
tbp.address1_input.input_text(addr1)
tbp.address2_input.input_text(addr2)
tbp.submit_button.click()

assert tbp.sab_name.text == f'Name:{name}'
assert tbp.sub_email.text == f'Email:{email}'
assert tbp.sub_address1.text == f'Current Address :{addr1}'
assert tbp.sub_address2.text == f'Permananet Address :{addr2}'
print(f'details:\n{name}\n{email}\n{addr1}\n{addr2}\n ALL CORRECT !!!')
browser.quit()