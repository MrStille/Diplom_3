import os
import sys

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators

sys.path.append(os.getcwd())
import random
import string


class Utils:

    @staticmethod
    def get_random_email():
        return f"test-{Utils.generate_random_string(4)}-@yandex.ru"

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # @staticmethod
    # def wait_element_visible(driver, locator):
    #     return WebDriverWait(driver, Utils.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
    #
    # @staticmethod
    # def wait_element_not_visible(driver, locator):
    #     return WebDriverWait(driver, Utils.DEFAULT_TIMEOUT).until(EC.invisibility_of_element_located(locator))
    #
    # @staticmethod
    # def wait_element_has_text(driver, locator, text):
    #     return WebDriverWait(driver, Utils.DEFAULT_TIMEOUT).until(EC.text_to_be_present_in_element(locator, str(text)))
    #
    #
    # @staticmethod
    # @allure.step("Move item to location")
    # def drag_item_to_basket(driver, from_locator):
    #     from_web_element = driver.find_element(*from_locator)
    #     driver.execute_script("arguments[0].scrollIntoView(true);", from_web_element)
    #     to_web_element = driver.find_element(*MainPageLocators.MAIN_BASKET)
    #     ac = ActionChains(driver)
    #     ac.drag_and_drop(from_web_element, to_web_element).pause(1).perform()