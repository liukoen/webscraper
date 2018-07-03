import requests
from selenium import webdriver
#import beautifulsoup4


url="**"
driver=webdriver.Chrome()
usern="** "
passwd = input("password")

driver.get(url)

links =[]
for a in driver.find_elements_by_xpath('.//a'):
    links.append(a.get_attribute("href"))

print(links)
try:
    driver.find_element_by_id("username").send_keys(usern)
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_id("btnSubmit_6").click()
    driver.find_element_by_link_text("Routz Timesheets/Synergy").click()
    driver.implicitly_wait(3)
    driver.find_element_by_link_text("Uren invoeren").click()
except:
    driver.find_element_by_id("btnContinue").click()
    driver.find_element_by_link_text("Routz Timesheets/Synergy").click()
    driver.implicitly_wait(3)
    driver.find_element_by_link_text("Uren invoeren").click()
    print("continue")







#driver.close()


