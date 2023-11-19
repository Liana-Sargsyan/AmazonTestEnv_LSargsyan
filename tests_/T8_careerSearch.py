import unittest
from selenium import webdriver
from pages_.footer import Footer
from pages_.amazonJobsPage import AmazonJobs
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class CareerSearching(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

    def test_career_searching_functionality(self):
        footerObj = Footer(self.driver)
        footerObj.click_to_careers_button()
        amazonJobsPageObj = AmazonJobs(self.driver)
        amazonJobsPageObj.fill_jobs_search_field("qa engineer")
        amazonJobsPageObj.click_to_search_submit_button()

        self.assertIn("qa+engineer", self.driver.current_url)

    def tearDown(self):
        self.driver.close()
