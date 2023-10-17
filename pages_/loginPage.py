from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


class LoginPage():
    def __init__(self, driver: webdriver):
        self.driver = driver


    def fill_username_field(self, username):
        usernameFieldElement = self.driver.find_element(By.ID, "ap_email")
        usernameFieldElement.clear()
        usernameFieldElement.send_keys(username)

    def click_to_continue_button(self):
        continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement.click()

    def fill_password_field(self, password):
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)

    def click_to_signin_button(self):
        sleep(6)
        signinButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signinButtonElement.click()
        sleep(6)
