import os
import sys


sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:
    RESTORE_BUTTON = (By.XPATH, '//form//button')
    RESTORE_EMAIL_INPUT = (By.XPATH, '//form//input')