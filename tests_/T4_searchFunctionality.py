import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from pages_.searchResultsPage import SearchResultsPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class SearchFunctionality(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

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

        self.assertEqual(searchResultsPageObj.validate_sort_by_dropdown_text(), "Sort by:Best Sellers", "Wrong Element Text")

    def tearDown(self):
        self.driver.close()
