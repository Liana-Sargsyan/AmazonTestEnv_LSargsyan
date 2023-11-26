from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class AmazonJobs(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.__jobsSearchFieldLocator = (By.XPATH, "(//input[@name='base_query']) [2]")
        self.__searchSubmitButtonLocator = (By.ID, "search-button")

    def fill_jobs_search_field(self, title):
        jobsSearchFieldElement = self._find_element(self.__jobsSearchFieldLocator)
        self._fill_field(jobsSearchFieldElement, title)

    def click_to_search_submit_button(self):
        searchSubmitButtonElement = self._find_element(self.__searchSubmitButtonLocator)
        self._click_to_element(searchSubmitButtonElement)
