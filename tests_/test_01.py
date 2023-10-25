from selenium import webdriver
from selenium.webdriver.common.by import By


import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


usernameFieldElement = driver.find_element(By.ID, "ap_email")
usernameFieldElement.clear()
usernameFieldElement.send_keys("lianasargsyan202@gmail.com")


continueButtonElement = driver.find_element(By.ID, "continue")
continueButtonElement.click()

passwordFieldElement = driver.find_element(By.ID, "ap_password")
passwordFieldElement.clear()
passwordFieldElement.send_keys("tracemalloc2023")

time.sleep(6)
signinButtonElement = driver.find_element(By.ID, "signInSubmit")
signinButtonElement.click()
time.sleep(6)

#time sleep on lines 25 and 28 is for avoiding CAPTCHA test.

driver.close()