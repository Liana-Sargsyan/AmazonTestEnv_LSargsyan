from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteLocator = (By.XPATH, "(//input[@value='Delete']) [1]")
        self.__cartCountValidationLocator = (By.ID, "nav-cart-count")
        self.__cartEmptinessMessageLocator = (By.XPATH, "(//div[@class='a-row']) [40]")
        self.__allProductsDeleteLocator = (By.XPATH, "(//input[@value='Delete'])")

    def delete_first_product_from_cart(self):
        firstProductDeleteElement = self._find_element(self.__firstProductDeleteLocator)
        self._click_to_element(firstProductDeleteElement)

    def validate_cart_count(self):
        cartCountElement = self._find_element(self.__cartCountValidationLocator)
        return self._get_element_text(cartCountElement)

    def validate_cart_emptiness_by_warning_message(self):
        cartEmptinessMessageElement = self._get_element_text_by_locator(self.__cartEmptinessMessageLocator)
        if cartEmptinessMessageElement == "Your Amazon Cart is empty.":
            return True
        else:
            return False

    def delete_all_products_from_cart(self):
        allProductsDeleteElements = self._find_elements(self.__allProductsDeleteLocator)
        for deleteButton in allProductsDeleteElements:
            deleteButton.click()
