from time import sleep
import os
import sys

import allure

from helpers.api_steps import ApiSteps
from helpers.utils import Utils
from locators.order_history_page_locators import OrderHistoryPageLocators

sys.path.append(os.getcwd())


class TestUserAccountPage:

    @allure.title("User accounts page opens from main page")
    def test_open_user_account_page(self, driver, main_page, good_user):
        ApiSteps.login(driver, good_user.get('email'), good_user.get('password'))
        user_page = main_page.click_user_account_link()
        user_page.wait_all_elements_visible()

    @allure.title("User logs out from account page")
    def test_logout(self, driver, user_account_page):
        log_in_page = user_account_page.click_logout()
        log_in_page.wait_page_loads()

    @allure.title("User opens his order history")
    def test_open_order_history(self, driver, user_account_page):
        order_history_page = user_account_page.click_orders_history()
        order_history_page.wait_page_loads()
        order_history_page.assert_orders_loaded()
