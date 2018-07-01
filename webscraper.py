import requests
from selenium import webdriver
#import beautifulsoup4



driver=webdriver.Chrome()

driver.get("http://nu.nl/")

links =[]

for a in driver.find_elements_by_xpath('.//a'):
    links.append(a.get_attribute("href"))


print(links)

driver.close()


