from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObject = LoginPage(driver)
loginPageObject.fill_username_field("lianasargsyan202@gmail.com")
loginPageObject.click_to_continue_button()
loginPageObject.fill_password_field("tracemalloc2023")
time.sleep(5)   #time sleep is for avoiding CAPTCHA test.
loginPageObject.click_to_signin_button()

navigationBarObject = NavigationBar(driver)
navigationBarObject.fill_search_field("headphones")
navigationBarObject.click_to_search_submit_button()

driver.close()