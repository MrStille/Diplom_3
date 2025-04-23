import os
import sys

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

class MenuLocators:
    MENU_USER_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')
    MENU_ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')
    MENU_ORDER_DESIGNER = (By.XPATH, '//p[text()="Конструктор"]')
