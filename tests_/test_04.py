from selenium import webdriver
from pages_.basePage import BasePage

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.amazon.com/")

basePageObject2 = BasePage(driver)

getTitle = basePageObject2._get_title()

print("The title is: ", getTitle)