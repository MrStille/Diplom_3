import os
import sys


sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    ORDER_ITEMS =  (By.XPATH, "//li[starts-with(@class,'OrderHistory_listItem')]")
    ORDER_BOX_PRICE = (By.XPATH, ORDER_ITEMS[1]+"[{0}]//div[starts-with(@class,'OrderHistory_dataBox')]//p")

