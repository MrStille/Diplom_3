import os
import sys

from helpers.api_steps import ApiSteps

sys.path.append(os.getcwd())
import allure


class TestOrderFeed:

    @allure.title("Open order feed from main page")
    def test_open_order_feed(self, main_page):
        main_page.click_order_feed_link_and_wait_page_loaded()

    @allure.title("Click on order in feed and check pop-up shows correct info")
    def test_open_order_details(self, order_feed_page):
        order_feed_page.click_order_in_list(0)
        order_feed_page.check_order_details_pop_up()

    @allure.title("Counter total increases after creating new order")
    def test_orders_total_counter_increases(self, order_feed_page, good_user):
         before_total = order_feed_page.get_total_orders_number()
         before_today = order_feed_page.get_today_orders_number()
         ApiSteps.create_new_order(good_user)
         order_feed_page.wait_total_number_is_changed(before_total)
         after_total = order_feed_page.get_total_orders_number()
         after_today = order_feed_page.get_today_orders_number()
         assert after_total > before_total
         assert after_today > before_today

    @allure.title("Created order gets in preparing order list")
    def test_new_order_gets_into_preparing_block(self, order_feed_page, good_user):
         created_order = ApiSteps.create_new_order(good_user)
         order_feed_page.check_order_in_preparing_list(created_order[1])

