from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count")
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchSubmitButtonLocator = (By.ID, "nav-search-submit-button")

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_element(cartButtonElement)

    def fill_search_field(self, text):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._click_to_element(searchFieldElement)
        self._fill_field(searchFieldElement, text)

    def click_to_search_submit_button(self):
        searchSubmitButton = self._find_element(self.__searchSubmitButtonLocator)
        self._click_to_element(searchSubmitButton)




