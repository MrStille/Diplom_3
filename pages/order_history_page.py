import os
import sys

import allure

from helpers.utils import Utils
from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage

sys.path.append(os.getcwd())


class OrderHistoryPage(BasePage):

    @allure.step('Wait until order block is loaded')
    def wait_page_loads(self):
        self.wait_element_visible(OrderHistoryPageLocators.ORDER_ITEMS)

    @allure.step("Get order history elements")
    def get_order_history_elements(self):
        elements = self.driver.find_elements(*OrderHistoryPageLocators.ORDER_ITEMS)
        return elements

    @allure.step('Get order price')
    def get_order_price(self, oder_position_id):
        order_item = (OrderHistoryPageLocators.ORDER_BOX_PRICE[0],
                      OrderHistoryPageLocators.ORDER_BOX_PRICE[1].format(oder_position_id))
        return float(self.driver.find_element(*order_item).text)

    @allure.step('Assert that order block is loaded and 1st item has price > 0')
    def assert_orders_loaded(self):
        elements = self.get_order_history_elements()
        assert len(elements) > 0
        assert self.get_order_price(1) > 0
