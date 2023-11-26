from pages_.navigationBarPage_.navigationBar import NavigationBar
from pages_.productRelatedPages_.searchResultsPage import SearchResultsPage
from pages_.productRelatedPages_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithoutLogIn


class ShareProductOnFacebook(BaseTestWithoutLogIn):

    def test_sharing_product_on_facebook(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("children books")
        navigationBarObj.click_to_search_submit_button()
        searchResulsPageObj = SearchResultsPage(self.driver)
        searchResulsPageObj.click_to_first_product()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.click_to_share_button()
        productDetailsPageObj.click_to_facebook_option()
