from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogIn


class SignOut(BaseTestWithLogIn):
    def test_account_sign_out(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.mouse_move_to_account_box()
        navigationBarObj.click_to_sigh_out_element()

        self.assertEqual(self.driver.title, "Amazon Sign-In")
