from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteLocator = (By.XPATH, "(//input[@value='Delete']) [1]")

    def delete_first_product_from_cart(self):
        firstProductDeleteElement = self._find_element(self.__firstProductDeleteLocator)
        self._click_to_element(firstProductDeleteElement)
