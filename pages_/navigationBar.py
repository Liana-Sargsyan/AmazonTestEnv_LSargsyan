from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_to_cart_button(self):
        # cartButtonElement = self.driver.find_element(By.ID, 'nav-cart-count')
        cartButtonElement = self._find_element(By.ID, "nav-cart-count")
        self._click_to_element(cartButtonElement)
        # cartButtonElement.click()

    def fill_search_field(self, text):
        searchFieldElement = self._find_element(By.ID, "twotabsearchtextbox")
        self._click_to_element(searchFieldElement)
        self._fill_field(searchFieldElement, text)

    def click_to_search_submit_button(self):
        searchSubmitButton = self._find_element(By.ID, "nav-search-submit-button")
        self._click_to_element(searchSubmitButton)




