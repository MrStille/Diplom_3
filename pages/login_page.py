import os
import sys

import allure

from helpers.utils import Utils
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

sys.path.append(os.getcwd())


class LoginPage(BasePage):

    @allure.step("Wait all login page elements are loaded")
    def wait_page_loads(self):
        self.wait_element_visible(LoginPageLocators.FORGOT_PASSWORD)
        self.wait_element_visible(LoginPageLocators.ENTER_LABEL)
        self.wait_element_visible(LoginPageLocators.ENTER_BUTTON)