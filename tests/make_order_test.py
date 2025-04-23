import os
import sys
sys.path.append(os.getcwd())

import allure



@allure.epic('Make order')
class TestMakeOrder:

    @allure.title("Ingredients pop up is opened and title has correct name")
    def test_pop_shown_when_click_on_ingredient(self, main_page):
        main_page.click_random_bun()
        main_page.wait_pop_up_visible()
        main_page.close_pop_up()

    @allure.title("Make simple order")
    def test_make_simple_order(self, main_page, good_user ):
        main_page.login(good_user)
        bun_id = main_page.put_random_bun_in_order()
        main_page.check_ingredient_count(bun_id, 2)
        sauce_id = main_page.put_random_sauce_in_order()
        main_page.check_ingredient_count(sauce_id, 1)
        main_id = main_page.put_random_main_in_order()
        main_page.check_ingredient_count(main_id, 1)
        main_page.click_order_button()
        main_page.check_order_number()
