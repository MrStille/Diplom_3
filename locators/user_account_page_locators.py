import os
import sys

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By


class UserAccountPageLocators:
    PROFILE_LABEL = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LABEL = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
