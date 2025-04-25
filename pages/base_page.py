import os
import sys

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators

sys.path.append(os.getcwd())

class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Move item to location")
    def drag_item_to_basket(self,from_locator):
        from_web_element = self.driver.find_element(*from_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", from_web_element)
        to_web_element = self.driver.find_element(*MainPageLocators.MAIN_BASKET)
        ac = ActionChains(self.driver)
        ac.drag_and_drop(from_web_element, to_web_element).pause(1).perform()

    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def wait_element_not_visible(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.invisibility_of_element_located(locator))

    def wait_element_has_text(self, locator, text):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.text_to_be_present_in_element(locator, str(text)))

    def wait_util_element_text_changes(self, locator, text):
       return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(lambda  drv: drv.find_element(*locator).text != str(text))
