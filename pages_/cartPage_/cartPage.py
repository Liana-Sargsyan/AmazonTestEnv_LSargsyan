from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteLocator = (By.XPATH, "(//input[@value='Delete']) [1]")
        self.__cartEmptinessMessageLocator = (By.XPATH, "(//div[@class='a-row']) [40]")
        self.__allProductsDeleteLocator = (By.XPATH, "(//input[@value='Delete'])")

    def delete_first_product_from_cart(self):
        firstProductDeleteElement = self._find_element(self.__firstProductDeleteLocator)
        self._click_to_element(firstProductDeleteElement)

    def validate_cart_emptiness_by_warning_message(self):
        cartEmptinessMessageElement = self._get_element_text_by_locator(self.__cartEmptinessMessageLocator)
        if cartEmptinessMessageElement == "Your Amazon Cart is empty.":
            logger("INFO", "Your cart is empty")

        else:
            logger("INFO:", "Your cart is not empty")
            exit(4)

    def delete_all_products_from_cart(self):
        from pages_.navigationBarPage_.navigationBar import NavigationBar
        navigationBarObj = NavigationBar(self.driver)
        while int(navigationBarObj.get_cart_count()) != 0:
            firstProductDeleteElement = self._find_element(self.__firstProductDeleteLocator)
            self._click_to_element(firstProductDeleteElement)
