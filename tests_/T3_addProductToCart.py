import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from pages_.searchResultsPage import SearchResultsPage
from pages_.productDetailsPage import ProductDetailsPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
import time


class AddProductToCart(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("lianasargsyan202@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("tracemalloc2023")
        time.sleep(5)  # time sleep is for avoiding CAPTCHA test.
        loginPageObj.click_to_signin_button()
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("psychology handbooks")
        navigationBarObj.click_to_search_submit_button()
        searchResulsPageObj = SearchResultsPage(self.driver)
        searchResulsPageObj.click_to_first_product()

    def test_add_product_to_cart(self):
        productDetailsPageObj = ProductDetailsPage(self.driver)
        cartPageObj = CartPage(self.driver)
        cartCountBeforeAdding = int(cartPageObj.validate_cart_count())
        productDetailsPageObj.click_to_add_to_cart_button()
        cartCountAfterAdding = int(cartPageObj.validate_cart_count())

        self.assertEqual(cartCountAfterAdding, cartCountBeforeAdding + 1, "Not Added to Cart")

    def tearDown(self):
        self.driver.close()
