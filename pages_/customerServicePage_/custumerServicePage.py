from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CustomerService(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.__shippingAndDeliveryButtonLocator = (By.XPATH, "//label[@for='foresight-help-topic-2']")
        self.__deliveryGuaranteesButtonLocator = (By.XPATH, "(//div[@class='fs-match-card-title'])[13]")

    def click_to_shipping_and_delivery_button(self):
        shippingAndDeliveryButtonElement = self._find_element(self.__shippingAndDeliveryButtonLocator)
        self._click_to_element(shippingAndDeliveryButtonElement)

    def click_to_delivery_guarantees_button(self):
        deliveryGuaranteesButtonElement = self._find_element(self.__deliveryGuaranteesButtonLocator)
        self._click_to_element(deliveryGuaranteesButtonElement)
