import os
import sys

import allure

from helpers.utils import Utils
from locators.login_page_locators import LoginPageLocators
from locators.restore_password_page_locators import RestorePasswordPageLocators as Rl
from pages.reset_password_page import ResetPasswordPage

sys.path.append(os.getcwd())
from data import Data


class RestorePasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self._wait_page_loads()

    @allure.step("Open restore password page")
    def _wait_page_loads(self):
        self.driver.get(Data.LOGIN_PAGE_URL)
        Utils.wait_element_visible(self.driver, LoginPageLocators.FORGOT_PASSWORD).click()
        Utils.wait_element_visible(self.driver, Rl.RESTORE_BUTTON)

    @allure.step("Enter text into email field")
    def enter_email(self, email):
        Utils.wait_element_visible(self.driver, Rl.RESTORE_EMAIL_INPUT).is_displayed()
        self.driver.find_element(*Rl.RESTORE_EMAIL_INPUT).send_keys(email)

    @allure.step("Click restore button")
    def click_restore_button(self):
        self.driver.find_element(*Rl.RESTORE_BUTTON).click()
        reset_password_page = ResetPasswordPage(self.driver)
        return reset_password_page
