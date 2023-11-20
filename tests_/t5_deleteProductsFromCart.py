from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from tests_.baseTest import BaseTestWithLogIn


class DeleteProductsFromCart(BaseTestWithLogIn):

    def test_validate_emptiness_of_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.driver)
        warningMessageOfCartEmptiness = cartPageObj.validate_cart_emptiness_by_warning_message()
        self.assertTrue(warningMessageOfCartEmptiness, "ERROR: validation failed")

    def test_delete_first_product_from_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        cartPageObj = CartPage(self.driver)
        cartCountBeforeDeletion = int(navigationBarObj.get_cart_count())
        if int(navigationBarObj.get_cart_count()) >= 1:
            cartPageObj.delete_first_product_from_cart()
        else:
            print("Warning: Your Amazon Cart is empty.")
        cartCountAfterDeletion = int(navigationBarObj.get_cart_count())

        self.assertEqual(cartCountAfterDeletion, cartCountBeforeDeletion - 1, "Unsuccessful Deletion")

    def test_delete_all_products_from_cart(self):
        cartPageObj = CartPage(self.driver)
        cartPageObj.delete_all_products_from_cart()
