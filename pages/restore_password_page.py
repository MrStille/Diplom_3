import os
import sys

import allure

from locators.login_page_locators import LoginPageLocators
from locators.restore_password_page_locators import RestorePasswordPageLocators as Rl
from pages.base_page import BasePage
from pages.reset_password_page import ResetPasswordPage

sys.path.append(os.getcwd())
from data import Data


class RestorePasswordPage(BasePage):

    @allure.step("Open restore password page")
    def open_page(self):
        self.driver.get(Data.LOGIN_PAGE_URL)
        self.wait_element_visible(LoginPageLocators.FORGOT_PASSWORD).click()
        self.wait_element_visible(Rl.RESTORE_BUTTON)

    @allure.step("Enter text into email field")
    def enter_email(self, email):
        self.wait_element_visible(Rl.RESTORE_EMAIL_INPUT).is_displayed()
        self.driver.find_element(*Rl.RESTORE_EMAIL_INPUT).send_keys(email)

    @allure.step("Click restore button")
    def click_restore_button(self):
        self.driver.find_element(*Rl.RESTORE_BUTTON).click()
        reset_password_page = ResetPasswordPage(self.driver)
        return reset_password_page
