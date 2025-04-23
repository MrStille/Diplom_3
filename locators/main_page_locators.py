import os
import sys

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//form//button')
    ORDER_BUTTONS = (By.XPATH, "//button[text()='Оформить заказ']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    BUNS_ITEMS = (By.XPATH, "//h2[text()='Булки']/parent::div/ul[1]/a")
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")
    SAUCE_ITEMS = (By.XPATH, "//h2[text()='Соусы']/parent::div/ul[2]/a")
    MAIN_TAB = (By.XPATH, "//span[text()='Начинка']")
    MAIN_ITEMS = (By.XPATH, "//h2[text()='Начинка']/parent::div/ul[3]/a")
    MAIN_BASKET = (By.XPATH, "//li[starts-with(@class,'BurgerConstructor_basket__listItem')]")

    INGREDIENT_BY_ID = (By.XPATH, "//a[contains(@href,'{0}')]")
    INGREDIENT_QUANTITY = (By.XPATH, "//a[contains(@href,'{0}')]/div")
    INGREDIENT_POP_UP = (By.XPATH, "//section[starts-with(@class,'Modal_modal_opened')]")
    INGREDIENT_POP_UP_TITLE = (By.XPATH, INGREDIENT_POP_UP[1] + "//h2")
    INGREDIENT_POP_UP_BUTTON = (By.XPATH, INGREDIENT_POP_UP[1] + "//button")

    ORDER_ID_LABEL = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_ID_NUMBER = (By.XPATH, ORDER_ID_LABEL[1] + "/parent::div/h2")
