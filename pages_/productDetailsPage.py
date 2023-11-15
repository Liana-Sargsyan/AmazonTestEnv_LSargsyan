from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonLocator = (By.ID, "submit.add-to-cart")
        self.__shareButtonLocator = (By.XPATH, "//div[@class='ssf-background-float']")
        self.__sharingOnFacebookOptionLocator = (By.CLASS_NAME, "fb-label")

    def click_to_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.__addToCartButtonLocator)
        self._click_to_element(addToCartButtonElement)
    def click_to_share_button(self):
        shareButtonElement = self._find_element(self.__shareButtonLocator)
        self._click_to_element(shareButtonElement)
    def click_to_facebook_option(self):
        facebookOptionElement = self._find_element(self.__sharingOnFacebookOptionLocator)
        self._click_to_element(facebookOptionElement)



