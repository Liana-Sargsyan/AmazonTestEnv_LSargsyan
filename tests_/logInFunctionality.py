import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener

import time


class LogIn(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_login(self):
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("lianasargsyan202@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("tracemalloc2023")
        time.sleep(5)  # time sleep is for avoiding CAPTCHA test.
        loginPageObj.click_to_signin_button()

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_negative_login(self):
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("lianasargsyan202@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("abcdef") # invalid password is given
        time.sleep(5)  # time sleep is for avoiding CAPTCHA test.
        loginPageObj.click_to_signin_button()

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def tearDown(self):
        self.driver.close()
