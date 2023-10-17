from selenium.webdriver.common.by import By

class CartPage():
    def __init__(self, driver):
        self.driver = driver

    def delete_first_product_from_cart(self):
        firstProductDeleteElement = self.driver.find_element(By.XPATH, "(//input[@value='Delete']) [1]")
        firstProductDeleteElement.click()