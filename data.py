import os
import sys
sys.path.append(os.getcwd())
class Data:
    SITE_URL = "https://stellarburgers.nomoreparties.site/"
    FORGOT_PASSWORD_PAGE_URL = SITE_URL + "forgot-password"
    LOGIN_PAGE_URL = SITE_URL + "login"
    ACCOUNT_PAGE_URL = SITE_URL + "account/profile"

    API_URL = 'https://stellarburgers.nomoreparties.site/api/'
    API_LOGIN_URL = API_URL + "auth/login"
    API_INGREDIENTS_URL = API_URL + "ingredients"
    API_ORDER_URL = API_URL + "orders"


