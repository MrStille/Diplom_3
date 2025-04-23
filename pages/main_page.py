import os
import random
import sys

import allure
from selenium.webdriver import ActionChains

from helpers.api_steps import ApiSteps
from helpers.utils import Utils
from locators.main_page_locators import MainPageLocators
from locators.menu_locators import MenuLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.user_account_page_locators import UserAccountPageLocators
from pages.order_feed_page import OrderFeedPage
from pages.user_account_page import UserAccountPage

sys.path.append(os.getcwd())
from data import Data


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.open_main_page()

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.driver.get(Data.SITE_URL)

    @allure.step("User logs in")
    def login(self, user):
        ApiSteps.login(self.driver, user.get("email"), user.get("password"))

    @allure.step("Click user account link on main page")
    def click_user_account_link(self):
        Utils.wait_element_visible(self.driver, MenuLocators.MENU_USER_ACCOUNT).click()
        Utils.wait_element_visible(self.driver, UserAccountPageLocators.EXIT_BUTTON)
        return UserAccountPage(self.driver)

    @allure.step("Click on random bun")
    def click_random_bun(self):
        Utils.wait_element_visible(self.driver, MainPageLocators.BUNS_TAB)
        buns = self.driver.find_elements(*MainPageLocators.BUNS_ITEMS)
        selected_bun = random.choice(buns)
        selected_bun.click()
        print(1)

    @allure.step("Select random bun and put in order")
    def put_random_bun_in_order(self):
        random_bun = ApiSteps.get_random_ingredient("bun")
        Utils.wait_element_visible(self.driver, MainPageLocators.MAIN_BASKET)
        bun = Utils.get_ingredient_locator(random_bun.get("_id"))
        Utils.drag_item_to_basket(self.driver, bun)
        return random_bun.get("_id")

    @allure.step("Select random sauce and put it in order")
    def put_random_sauce_in_order(self):
        random_sauce = ApiSteps.get_random_ingredient("sauce")
        Utils.wait_element_visible(self.driver, MainPageLocators.MAIN_BASKET)
        sauce = Utils.get_ingredient_locator(random_sauce.get("_id"))
        Utils.drag_item_to_basket(self.driver, sauce)
        return random_sauce.get("_id")

    @allure.step("Select random meat and put it in order")
    def put_random_main_in_order(self):
        random_main = ApiSteps.get_random_ingredient("main")
        Utils.wait_element_visible(self.driver, MainPageLocators.MAIN_BASKET)
        main = Utils.get_ingredient_locator(random_main.get("_id"))
        Utils.drag_item_to_basket(self.driver, main)
        return random_main.get("_id")

    @allure.step("Click order button")
    def click_order_button(self):
        Utils.wait_element_visible(self.driver, MainPageLocators.ORDER_BUTTONS).click()
        Utils.wait_element_visible(self.driver, MainPageLocators.ORDER_ID_LABEL)

    @allure.step("Check order number is positive")
    def check_order_number(self):
        order_number = Utils.wait_element_visible(self.driver, MainPageLocators.ORDER_ID_NUMBER).text
        assert int(order_number) > 0

    @allure.step("Check ingredient count")
    def check_ingredient_count(self, hash_id, cnt_expected):
        locator = (MainPageLocators.INGREDIENT_QUANTITY[0], MainPageLocators.INGREDIENT_QUANTITY[1].format(hash_id))
        cnt_actual = int(self.driver.find_element(*locator).text)
        assert cnt_expected == cnt_actual


    @allure.step("Select random sauce in order")
    def click_random_sauce(self):
        Utils.wait_element_visible(self.driver, MainPageLocators.BUNS_ITEMS)
        buns = self.driver.find_elements(*MainPageLocators.BUNS_ITEMS)
        selected_bun = random.choice(buns)
        selected_bun.click()

    @allure.step("Wait ingredient pop up is loaded and assert title")
    def wait_pop_up_visible(self):
        Utils.wait_element_visible(self.driver, MainPageLocators.INGREDIENT_POP_UP)
        title = Utils.wait_element_visible(self.driver, MainPageLocators.INGREDIENT_POP_UP_TITLE).text
        assert title == 'Детали ингредиента'

    @allure.step("Close ingredient pop-up and wait till it closes")
    def close_pop_up(self):
        Utils.wait_element_visible(self.driver, MainPageLocators.INGREDIENT_POP_UP_BUTTON).click()
        Utils.wait_element_not_visible(self.driver, MainPageLocators.INGREDIENT_POP_UP_BUTTON)

    @allure.step("Click order feed menu button")
    def click_order_feed_link_and_wait_page_loaded(self):
        Utils.wait_element_visible(self.driver, MenuLocators.MENU_ORDER_FEED).click()
        Utils.wait_element_visible(self.driver, OrderFeedPageLocators.PAGE_TITLE)
        return OrderFeedPage(self.driver)
