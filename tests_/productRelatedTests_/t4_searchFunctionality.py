from pages_.navigationBarPage_.navigationBar import NavigationBar
from pages_.productRelatedPages_.searchResultsPage import SearchResultsPage
from tests_.baseTest import BaseTestWithoutLogIn


class SearchFunctionality(BaseTestWithoutLogIn):

    def test_relevant_search_results(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("headphones")
        navigationBarObj.click_to_search_submit_button()

        self.assertEqual(self.driver.title, "Amazon.com : headphones")

    def test_sorted_search_results_by_best_sellers(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("sunglasses")
        navigationBarObj.click_to_search_submit_button()
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj.click_to_sort_by_dropdown()
        searchResultsPageObj.click_to_best_seller_option()

        self.assertEqual(searchResultsPageObj.validate_sort_by_dropdown_text(), "Sort by:Best Sellers",
                         "Wrong Element Text")
