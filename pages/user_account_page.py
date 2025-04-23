import os
import sys

import allure

from helpers.api_steps import ApiSteps
from helpers.utils import Utils
from locators.user_account_page_locators import UserAccountPageLocators
from pages.login_page import LoginPage
from pages.order_history_page import OrderHistoryPage

sys.path.append(os.getcwd())


@allure.epic('User Account Page')
class UserAccountPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Wait util user's account page elements are loaded")
    def wait_all_elements_visible(self):
        Utils.wait_element_visible(self.driver, UserAccountPageLocators.PROFILE_LABEL)
        Utils.wait_element_visible(self.driver, UserAccountPageLocators.ORDER_HISTORY_LABEL)
        Utils.wait_element_visible(self.driver, UserAccountPageLocators.EXIT_BUTTON)

    @allure.step("Login through api and open user account page")
    def login_and_open_page(self, user, main_page):
        ApiSteps.login(self.driver, user.get('email'), user.get('password'))
        main_page.click_user_account_link()
        self.wait_all_elements_visible()

    @allure.step("Click logout button")
    def click_logout(self):
        Utils.wait_element_visible(self.driver, UserAccountPageLocators.EXIT_BUTTON).click()
        return LoginPage(self.driver)

    @allure.step("Click order history link")
    def click_orders_history(self):
        Utils.wait_element_visible(self.driver, UserAccountPageLocators.ORDER_HISTORY_LABEL).click()
        return OrderHistoryPage(self.driver)
