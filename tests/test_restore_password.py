import os
import re
import sys

import allure

sys.path.append(os.getcwd())
@allure.epic('Restore password')
class TestsRestorePassword:
    @allure.title("Open Restore page")
    def test_enter_email(self, driver, restore_password_page, good_user):
        restore_password_page.enter_email(good_user.get('email'))
        reset_password_page = restore_password_page.click_restore_button()
        reset_password_page.wait_page_loads()

    @allure.title("Enter new password and check it is hidden")
    def test_enter_new_password(self, driver, restore_password_page, good_user):
        restore_password_page.enter_email(good_user.get('email'))
        reset_password_page = restore_password_page.click_restore_button()
        new_password = "NewPassword1"
        reset_password_page.type_new_password(new_password)
        hidden_password = reset_password_page.get_new_password_value()
        hidden_password_type = reset_password_page.get_new_password_type_attribute()
        reset_password_page.click_show_password_switcher()
        visible_password_type =  reset_password_page.get_new_password_type_attribute()

        assert hidden_password == new_password
        assert hidden_password_type == 'password'
        assert visible_password_type == 'text'










