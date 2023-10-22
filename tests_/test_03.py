from selenium import webdriver
from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.amazon.com/")

basePageObject = BasePage(driver)


signInButtonText = driver.find_element(By.ID, "nav-link-accountList")
basePageObject._get_element_text(signInButtonText)

