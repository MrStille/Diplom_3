import os
import sys

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD = (By.XPATH,"//a[@href = '/forgot-password']")
    ENTER_BUTTON = (By.XPATH,"//button[text() = 'Войти']")
    ENTER_LABEL = (By.XPATH,"//h2[text() = 'Вход']")