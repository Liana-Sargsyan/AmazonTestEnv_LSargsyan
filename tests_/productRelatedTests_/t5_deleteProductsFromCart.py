from pages_.navigationBarPage_.navigationBar import NavigationBar
from pages_.cartPage_.cartPage import CartPage
from tests_.baseTest import BaseTestWithLogIn
from pages_.productRelatedPages_.searchResultsPage import SearchResultsPage
from pages_.productRelatedPages_.productDetailsPage import ProductDetailsPage


class DeleteProductsFromCart(BaseTestWithLogIn):

    def test_validate_emptiness_of_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.driver)
        cartPageObj.validate_cart_emptiness_by_warning_message()

    def test_delete_first_product_from_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        if int(navigationBarObj.get_cart_count()) >= 1:
            cartCountBeforeDeletion = int(navigationBarObj.get_cart_count())
            navigationBarObj.click_to_cart_button()
            cartPageObj = CartPage(self.driver)
            cartPageObj.delete_first_product_from_cart()
            cartCountAfterDeletion = int(navigationBarObj.get_cart_count())
        else:
            navigationBarObj.fill_search_field("psychology handbooks")
            navigationBarObj.click_to_search_submit_button()
            searchResulsPageObj = SearchResultsPage(self.driver)
            searchResulsPageObj.click_to_first_product()
            productDetailsPageObj = ProductDetailsPage(self.driver)
            productDetailsPageObj.click_to_add_to_cart_button()
            cartCountBeforeDeletion = int(navigationBarObj.get_cart_count())
            navigationBarObj.click_to_cart_button()
            cartPageObj = CartPage(self.driver)
            cartPageObj.delete_first_product_from_cart()
            cartCountAfterDeletion = int(navigationBarObj.get_cart_count())

        self.assertEqual(cartCountAfterDeletion, cartCountBeforeDeletion - 1, "Unsuccessful Deletion")

    def test_delete_all_products_from_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.driver)
        cartCountBeforeDeletion = int(navigationBarObj.get_cart_count())
        cartPageObj.delete_all_products_from_cart()
        cartCountAfterDeletion = int(navigationBarObj.get_cart_count())

        self.assertEqual(cartCountAfterDeletion, 0, "Unsuccessful Deletion")
