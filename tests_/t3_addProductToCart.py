from pages_.navigationBar import NavigationBar
from pages_.searchResultsPage import SearchResultsPage
from pages_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogIn


class AddProductToCart(BaseTestWithLogIn):
    def test_add_product_to_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("psychology handbooks")
        navigationBarObj.click_to_search_submit_button()
        searchResulsPageObj = SearchResultsPage(self.driver)
        searchResulsPageObj.click_to_first_product()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        cartCountBeforeAdding = int(navigationBarObj.get_cart_count())
        productDetailsPageObj.click_to_add_to_cart_button()
        cartCountAfterAdding = int(navigationBarObj.get_cart_count())

        self.assertEqual(cartCountAfterAdding, cartCountBeforeAdding + 1, "Not Added to Cart")
