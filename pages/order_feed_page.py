import os
import sys
from time import sleep

import allure

from helpers.utils import Utils
from locators.order_feed_page_locators import OrderFeedPageLocators

sys.path.append(os.getcwd())


class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_in_list(self, position_id):
        allure.step(f"Get random ingredient of {position_id}")
        Utils.wait_element_visible(self.driver, OrderFeedPageLocators.ORDERS_LIST)
        self.driver.find_elements(*OrderFeedPageLocators.ORDERS_LIST)[position_id].click()

    @allure.step("Check order details pop up")
    def check_order_details_pop_up(self):
        order_id = Utils.wait_element_visible(self.driver, OrderFeedPageLocators.ORDERS_POPUP_ID).text
        order_price = Utils.wait_element_visible(self.driver, OrderFeedPageLocators.ORDERS_POPUP_PRICE).text
        order_ingredients = self.driver.find_elements(*OrderFeedPageLocators.ORDERS_POPUP_INGREDIENTS)
        assert int(order_id.replace("#",'')) > 0
        assert int(order_price) > 0
        assert len(order_ingredients) > 0

    @allure.step("Get total orders number")
    def get_total_orders_number(self):
        Utils.wait_element_visible(self.driver, OrderFeedPageLocators.ORDERS_TOTAL_NUMBERS)
        return int(self.driver.find_elements(*OrderFeedPageLocators.ORDERS_TOTAL_NUMBERS)[0].text)

    @allure.step("Get today orders number")
    def get_today_orders_number(self):
        Utils.wait_element_visible(self.driver, OrderFeedPageLocators.ORDERS_TOTAL_NUMBERS)
        return int(self.driver.find_elements(*OrderFeedPageLocators.ORDERS_TOTAL_NUMBERS)[1].text)

    @allure.step("Check order in preparing orders list")
    def check_order_in_preparing_list(self, order_id):
        Utils.wait_element_has_text(self.driver, OrderFeedPageLocators.PREPARING_ORDER_BLOCK, order_id)
        orders = self.driver.find_elements(*OrderFeedPageLocators.PREPARING_ORDERS)
        assert len(orders) > 0
        is_order_found = False
        for order in orders:
            try:
                preparing_order_id = int(order.text)
            except ValueError:
                continue
            if preparing_order_id == order_id:
                is_order_found = True
                break
        assert is_order_found is True




    @allure.step("Reload order feed page")
    def reload(self):
        self.driver.refresh()

