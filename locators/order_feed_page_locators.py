import os
import sys

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    PAGE_TITLE = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDERS_LIST = (By.XPATH, "//li[starts-with(@class, 'OrderHistory_listItem')]")
    ORDERS_POPUP = (By.XPATH, "//div[starts-with(@class, 'Modal_orderBox')]")
    ORDERS_TOTAL_NUMBERS = (By.XPATH, "//p[starts-with(@class, 'OrderFeed_number')]")
    PREPARING_ORDER_BLOCK = (By.XPATH, "//ul[starts-with(@class, 'OrderFeed_orderListReady')]")
    PREPARING_ORDERS = (By.XPATH, "//ul[starts-with(@class, 'OrderFeed_orderListReady')]/li")
    ORDERS_POPUP_ID = (By.XPATH, ORDERS_POPUP[1]+"/p")
    ORDERS_POPUP_TITLE = (By.XPATH, ORDERS_POPUP[1]+"//h2")
    ORDERS_POPUP_INGREDIENTS = (By.XPATH, ORDERS_POPUP[1]+"//li[starts-with(@class, 'Modal_listItem')]")
    ORDERS_POPUP_PRICE = (By.XPATH, ORDERS_POPUP[1]+"//div[starts-with(@class, 'Modal_priceBox')]/p")

