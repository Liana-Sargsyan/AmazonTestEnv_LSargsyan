from pages_.footer import Footer
from pages_.custumerServicePage import CustomerService
from tests_.baseTest import BaseTestWithoutLogIn


class DeliveryGuarantees(BaseTestWithoutLogIn):

    def test_delivery_guarantees_help_info(self):
        footerObj = Footer(self.driver)
        footerObj.click_to_help_button()
        customerServicePageObj = CustomerService(self.driver)
        customerServicePageObj.click_to_shipping_and_delivery_button()
        customerServicePageObj.click_to_delivery_guarantees_button()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assertIn("Delivery Guarantees - Amazon Customer Service", self.driver.title, "Wrong Page Title")
