from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signinButtonLocator = (By.ID, "signInSubmit")
        self.__invalidPasswordErrorMessageLocator = (By.XPATH, "(//div[@class='a-box-inner a-alert-container'])[1]")
        self.__invalidUsernameErrorMessageLocator = (By.ID, "auth-error-message-box")

    def fill_username_field(self, username):
        usernameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(usernameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click_to_element(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_signin_button(self):
        signinButtonElement = self._find_element(self.__signinButtonLocator)
        self._click_to_element(signinButtonElement)

    def validate_invalid_password_error_message(self):
        errorMessageElement = self._get_element_text_by_locator(self.__invalidPasswordErrorMessageLocator)
        expectedErrorMessage = """There was a problem
Your password is incorrect"""
        if errorMessageElement == expectedErrorMessage:
            return True
        else:
            return False

    def validate_invalid_username_error_message(self):
        errorMessageElement = self._get_element_text_by_locator(self.__invalidUsernameErrorMessageLocator)
        expectedErrorMessage = """There was a problem
We cannot find an account with that email address"""
        if errorMessageElement == expectedErrorMessage:
            return True
        else:
            return False
