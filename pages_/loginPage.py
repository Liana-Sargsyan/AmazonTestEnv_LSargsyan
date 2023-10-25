from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: webdriver):
        self.driver = driver

    def fill_username_field(self, username):
        # usernameFieldElement = self.driver.find_element(By.ID, "ap_email")
        userNameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFieldElement, username)
        # userNameFieldElement.clear()
        # userNameFieldElement.send_keys(username)

    def click_to_continue_button(self):
        # continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click_to_element(continueButtonElement)
        # continueButtonElement.click()

    def fill_password_field(self, password):
        # passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFieldElement, password)
        # passwordFieldElement.clear()
        # passwordFieldElement.send_keys(password)

    def click_to_signin_button(self):
        # signinButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signinButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click_to_element(signinButtonElement)
        # signinButtonElement.click()