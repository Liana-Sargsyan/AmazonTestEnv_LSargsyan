from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductLocator = (By.XPATH, "(//span[@class ='a-size-medium a-color-base a-text-normal']) [1]")
        self.__sortByDropdownLocator = (By.XPATH, "//span[@class='a-button a-button-dropdown a-button-small']")
        self.__sortByBestSellersLocator = (By.ID, "s-result-sort-select_5")

    def click_to_first_product(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click_to_element(firstProductElement)

    def click_to_sort_by_dropdown(self):
        sortByDropdownElement = self._find_element(self.__sortByDropdownLocator)
        self._click_to_element(sortByDropdownElement)

    def click_to_best_seller_option(self):
        bestSellerOptionElement = self._find_element(self.__sortByBestSellersLocator)
        self._click_to_element(bestSellerOptionElement)

