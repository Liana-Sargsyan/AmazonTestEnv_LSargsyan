import unittest
from selenium import webdriver
from pages_.logInPage_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import validUser, mainPageUrl, signInPageUrl
import time


class BaseTestWithoutLogIn(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)


def tearDown(self):
    self.driver.close()


class BaseTestWithLogIn(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(validUser.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(5)  # time sleep is for avoiding CAPTCHA test.
        loginPageObj.click_to_signin_button()

    def tearDown(self):
        self.driver.close()
