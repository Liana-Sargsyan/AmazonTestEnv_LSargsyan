from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class Footer(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.__helpButtonLocator = (By.XPATH, "(//a[@class='nav_a']) [26]")
        self.__careersButtonLocator = (By.XPATH, "(//a[@class='nav_a']) [1]")

    def click_to_help_button(self):
        helpButtonElement = self._find_element(self.__helpButtonLocator)
        self._click_to_element(helpButtonElement)

    def click_to_careers_button(self):
        careersButtonElement = self._find_element(self.__careersButtonLocator)
        self._click_to_element(careersButtonElement)
