from pages.base_page import BasePage
from locators.base_locators import BasePageLocators


class OrderPage(BasePage):

    def click_to_order(self):
        self.open_page()
        self.click_to_element(BasePageLocators.order_id)