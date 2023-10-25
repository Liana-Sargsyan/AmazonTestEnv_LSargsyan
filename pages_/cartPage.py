from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def delete_first_product_from_cart(self):
        # firstProductDeleteElement = self.driver.find_element(By.XPATH, "(//input[@value='Delete']) [1]")
        firstProductDeleteElement = self._find_element(By.XPATH, "(//input[@value='Delete']) [1]")
        self._click_to_element(firstProductDeleteElement)
        # firstProductDeleteElement.click()
