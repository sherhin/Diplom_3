from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
class OrderPage(BasePage):

    def click_to_order(self):
        self.open_page()
        self.click_to_element(OrderPageLocators.ORDER_IN_ORDER_FEED)