from helpers_api.conftest import api_client
from helpers_api.helpers_api import HelpersApi as help_api
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    def test_check_order_in_order_page(self, order_page, api_client):
        order_page.open_page()
        order_id, order_ingredients = help_api.create_user_and_order(api_client)
        order_number = order_page.get_text_from_element(OrderPageLocators.ORDER_IN_ORDER_FEED)
        assert order_number == f'#0{order_id}'

    def test_click_to_order_and_check_pop_up(self, order_page, api_client):
        help_api.create_user_and_order(api_client)
        order_page.click_to_order()
        order_page.find_element_with_wait(OrderPageLocators.CONTAIN)
        order_ingredients = order_page.get_text_from_element(OrderPageLocators.CONTAINING_ELEMENTS)
        assert order_ingredients == order_ingredients

    def test_check_order_count_by_day(self, order_page, api_client):
        order_page.open_page()
        count_before = order_page.get_order_count_by_day()
        help_api.create_user_and_order(api_client)
        count_after = order_page.get_order_count_by_day()
        assert count_after == count_before + 1

    def test_check_all_orders_count(self, order_page, api_client):
        order_page.open_page()
        count_before = order_page.get_all_orders_count()
        help_api.create_user_and_order(api_client)
        count_after = order_page.get_all_orders_count()
        assert count_after == count_before + 1

    def test_check_order_in_work(self, order_page, api_client):
        order_page.open_page()
        order, ingredients = help_api.create_user_and_order(api_client)
        order_id = f'0{order}'
        order_in_list = order_page.wait_order_in_list()
        assert order_in_list == order_id



