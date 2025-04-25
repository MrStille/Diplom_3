import os
import sys
sys.path.append(os.getcwd())

import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Wait util all ResetPasswordPage elements are visible ')
    def wait_page_loads(self):
        self.wait_element_visible(ResetPasswordPageLocators.PASSWORD_INPUT)
        self.wait_element_visible(ResetPasswordPageLocators.CODE_INPUT)

    @allure.step('Type new password value')
    def type_new_password(self, password):
        self.wait_element_visible(ResetPasswordPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Get password type attribute value')
    def get_new_password_type_attribute(self):
        return self.wait_element_visible(ResetPasswordPageLocators.PASSWORD_INPUT).get_attribute('type')

    @allure.step('Get new password value')
    def get_new_password_value(self):
        return self.wait_element_visible(ResetPasswordPageLocators.PASSWORD_INPUT).get_attribute('value')

    @allure.step('Click on show password switcher')
    def click_show_password_switcher(self):
        self.wait_element_visible(ResetPasswordPageLocators.PASSWORD_INPUT_SWITCHER).click()
