import os
import random
import sys

import allure

sys.path.append(os.getcwd())
import requests

from data import Data


class ApiSteps:

    @staticmethod
    @allure.title("Login user using api request")
    def api_login(email, password):
        payload = {
            "email": email,
            "password": password,
        }
        response = requests.post(Data.API_LOGIN_URL, data=payload)
        access_token = response.json()['accessToken']
        refresh_token = response.json()['refreshToken']
        return access_token, refresh_token

    @staticmethod
    @allure.title("Login user in browser using api request")
    def login(driver, email, password):
        response = ApiSteps.api_login(email, password)
        access_token = response[0]
        refresh_token = response[1]
        driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")
        driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")
        driver.refresh()

    @staticmethod
    @allure.step("Get all ingredients")
    def all_ingredients():
        all_ingredients = {}
        ingredients = requests.get(Data.API_INGREDIENTS_URL).json()["data"]
        for ingredient in ingredients:
            if len(all_ingredients) <= 3:
                all_ingredients.setdefault(ingredient.get("type"), list())
            all_ingredients[ingredient.get("type")].append(ingredient)
        return all_ingredients

    @staticmethod
    def get_random_ingredient(i_type):
        all_ingredients = ApiSteps.all_ingredients()
        return random.choice(all_ingredients[i_type])

    @staticmethod
    @allure.step("Create new random order through api")
    def create_new_order(user):
        ingredients = ApiSteps.all_ingredients()
        bun = random.choice(ingredients["bun"])
        meat = random.choice(ingredients["main"])
        sauce = random.choice(ingredients["sauce"])
        payload = {
            "ingredients": [bun.get("_id"), sauce.get("_id"), meat.get("_id")],
        }
        login_user = ApiSteps.api_login(user.get("email"), user.get("password"))

        response = ApiSteps.create_order(login_user[0], payload)
        return response.json()["order"]["_id"], response.json()["order"]["number"]

    @staticmethod
    @allure.step("Send post request to create order through api")
    def create_order(access_token, payload):
        headers = {'Authorization': access_token}
        response = requests.post(Data.API_ORDER_URL, data=payload, headers=headers)
        return response