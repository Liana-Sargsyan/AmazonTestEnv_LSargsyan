from pages_.logInPage_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidUserName, userWithInvalidPassword, signInPageUrl
import time
from tests_.baseTest import BaseTestWithoutLogIn


class LogIn(BaseTestWithoutLogIn):
    def test_positive_login(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(validUser.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(5)  # time sleep is for avoiding CAPTCHA test.
        loginPageObj.click_to_signin_button()

        self.assertEqual(self.driver.title, "Amazon.com. Spend less. Smile more.")

    def test_negative_login_with_invalid_password(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidPassword.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(userWithInvalidPassword.password)
        time.sleep(5)  # time sleep is for avoiding CAPTCHA test.
        loginPageObj.click_to_signin_button()

        self.assertTrue(loginPageObj.validate_invalid_password_error_message(), "No error was found, but should be")

    def test_negative_login_with_invalid_username(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidUserName.userName)
        loginPageObj.click_to_continue_button()

        self.assertTrue(loginPageObj.validate_invalid_username_error_message(), "No error was found, but should be")
