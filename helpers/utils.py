import os
import sys

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators

sys.path.append(os.getcwd())
import random
import string


class Utils:

    @staticmethod
    def get_random_email():
        return f"test-{Utils.generate_random_string(4)}-@yandex.ru"

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string