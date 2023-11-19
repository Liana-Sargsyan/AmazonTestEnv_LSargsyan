import unittest
from selenium import webdriver
from pages_.footer import Footer
from pages_.custumerServicePage import CustomerService
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class DeliveryGuarantees(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

    def test_delivery_guarantees_help_info(self):
        footerObj = Footer(self.driver)
        footerObj.click_to_help_button()
        customerServicePageObj = CustomerService(self.driver)
        customerServicePageObj.click_to_shipping_and_delivery_button()
        customerServicePageObj.click_to_delivery_guarantees_button()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assertIn("Delivery Guarantees - Amazon Customer Service", self.driver.title, "Wrong Page Title")

    def tearDown(self):
        self.driver.close()
