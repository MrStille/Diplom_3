import os
import re
import sys

import allure

from helpers.utils import Utils
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.CODE_INPUT)

    @allure.step('Wait util all ResetPasswordPage elements are visible ')
    def wait_page_loads(self):
        Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.PASSWORD_INPUT)
        Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.CODE_INPUT)

    @allure.step('Type new password value')
    def type_new_password(self, password):
        Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Get password type attribute value')
    def get_new_password_type_attribute(self):
        return Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.PASSWORD_INPUT).get_attribute('type')

    @allure.step('Get new password value')
    def get_new_password_value(self):
        return Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.PASSWORD_INPUT).get_attribute('value')

    @allure.step('Click on show password switcher')
    def click_show_password_switcher(self):
        Utils.wait_element_visible(self.driver, ResetPasswordPageLocators.PASSWORD_INPUT_SWITCHER).click()
