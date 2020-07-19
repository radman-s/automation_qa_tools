from selenium import webdriver
from pages.web_table_page import WebTablePage

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)

wtp = WebTablePage(driver=browser)

first_n = ['#', 'Adam', 'Barbra', 'Coba', 'Daniel', 'Eva', 'Ferdinand', 'Gordon']
last_n = ['#', 'Anderson', 'Barnes', 'Cody', 'Daniels', 'Ember', 'Franz', 'Garrison']
email_table = ['#', 'anderson@gmail.com', 'barnes@gmail.com', 'cody@gmail.com', 'daniesl@gmail.com', 'ember@gmail.com', 'franz@gmail.com', 'garrison@gmail.com']
age = ['#', '50', '32', '21', '40', '45', '30', '27']
salary = ['#', '45000', '35000', '23000', '38000', '40000', '36000', '29000']
department = ['#', 'QA', 'Insurance', 'HR', 'Legal', 'Compliance', 'Accounts', 'Services']

wtp.go()

wtp.web_tables_button.click()
wtp.delete_record1.click()
wtp.delete_record2.click()
wtp.delete_record3.click()

# fill up the register 7 X
wtp.add_button.click()
i = 0
count = 0
while i < 7:
    i += 1
    wtp.first_name_table.input_text(first_n[i])
    wtp.last_name_table.input_text(last_n[i])
    wtp.email_table.input_text(email_table[i])
    wtp.age_table.input_text(age[i])
    wtp.salary_table.input_text(salary[i])
    wtp.department_table.input_text(department[i])
    wtp.submit_table.click()
    count += 1
    if count < 7:
        wtp.add_button.click()
    else:
        break

wtp.rows_drop.select_drop("5")
wtp.next_table.click()
wtp.previous_table.click()
browser.quit()


