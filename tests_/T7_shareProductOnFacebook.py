import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from pages_.searchResultsPage import SearchResultsPage
from pages_.productDetailsPage import ProductDetailsPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class ShareProductToFacebook(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("children books")
        navigationBarObj.click_to_search_submit_button()
        searchResulsPageObj = SearchResultsPage(self.driver)
        searchResulsPageObj.click_to_first_product()

    def test_sharing_product_on_facebook(self):
        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.click_to_share_button()
        productDetailsPageObj.click_to_facebook_option()

    def tearDown(self):
        self.driver.close()
