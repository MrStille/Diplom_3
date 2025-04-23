import os
import sys

import allure

from data import Data
from helpers.utils import Utils
from locators.login_page_locators import LoginPageLocators

sys.path.append(os.getcwd())


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Wait all login page elements are loaded")
    def wait_page_loads(self):
        Utils.wait_element_visible(self.driver, LoginPageLocators.FORGOT_PASSWORD)
        Utils.wait_element_visible(self.driver, LoginPageLocators.ENTER_LABEL)
        Utils.wait_element_visible(self.driver, LoginPageLocators.ENTER_BUTTON)

    @allure.step("Open login page")
    def open_login_page(self):
        self.driver.get(Data.LOGIN_PAGE_URL)
        Utils.wait_element_visible(self.driver, LoginPageLocators.FORGOT_PASSWORD).click()
        # Utils.wait_element_visible(self.driver, )

    @allure.step("Click forgot password link")
    def open_forgot_password_page(self):
        self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD).click()