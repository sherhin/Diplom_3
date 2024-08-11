import time

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
class OrderPage(BasePage):

    def click_to_order(self):
        self.open_page()
        self.click_to_element(OrderPageLocators.ORDER_IN_ORDER_FEED)

    def get_order_count_by_day(self):
        count = self.get_text_from_element(OrderPageLocators.COMPLETED_ORDERS_TODAY_BEFORE)
        return int(count)

    def get_all_orders_count(self):
        count = self.get_text_from_element(OrderPageLocators.ALL_ORDERS_COUNT)
        return int(count)

    def wait_order_in_list(self):
        previous_value = 'Все текущие заказы готовы!'
        current_value = 'Все текущие заказы готовы!'
        while current_value == previous_value:
            current_value = self.get_text_from_element(OrderPageLocators.ORDER_LIST)
            time.sleep(1)
        return current_value

