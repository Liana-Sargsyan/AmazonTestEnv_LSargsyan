from pages_.footerPage_.footer import Footer
from pages_.jobsPage_.amazonJobsPage import AmazonJobs
from tests_.baseTest import BaseTestWithoutLogIn


class CareerSearching(BaseTestWithoutLogIn):

    def test_career_searching_functionality(self):
        footerObj = Footer(self.driver)
        footerObj.click_to_careers_button()
        amazonJobsPageObj = AmazonJobs(self.driver)
        amazonJobsPageObj.fill_jobs_search_field("qa engineer")
        amazonJobsPageObj.click_to_search_submit_button()

        self.assertIn("qa+engineer", self.driver.current_url)
