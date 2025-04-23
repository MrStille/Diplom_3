import pytest
import os
import sys

from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage
from pages.user_account_page import UserAccountPage
from pages.main_page import MainPage

sys.path.append(os.getcwd())
from selenium import webdriver

from data import Data


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.SITE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def order_feed_page(main_page):
    return main_page.click_order_feed_link_and_wait_page_loaded()


@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture()
def restore_password_page(driver):
    return RestorePasswordPage(driver)


@pytest.fixture()
def user_account_page(driver, main_page, good_user):
    user_account_page = UserAccountPage(driver)
    user_account_page.login_and_open_page(good_user, main_page)
    return user_account_page


@pytest.fixture()
def good_user():
    return {
        "email": "kmikhalev18303@ya.ru",
        "password": "Sun2009",
    }
