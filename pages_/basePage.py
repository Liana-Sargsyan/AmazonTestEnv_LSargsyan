from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except:
            print("Element not found")
            exit(1)

    def _click_to_element(self, webElement):
        webElement.click()

    def _get_title(self):
        return self.driver.title

    def _fill_field(self, element, text):
        element.clear()
        element.send_keys(text)

    def _get_element_text(self, webElement):
        return webElement.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

    def _mouse_move(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
