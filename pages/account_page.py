
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data import Urls


class AccountPage(BasePage):

    def logout(self):
        self.click_to_element(AccountPageLocators.EXIT_BUTTON)
        self.wait_for_url_change(Urls.MAIN_PAGE+Urls.AUTHORIZATION_PAGE)

    def move_to_order_history(self):
        self.click_to_element(AccountPageLocators.ORDERS_HISTORY)
        self.wait_for_url_change(Urls.MAIN_PAGE+Urls.ORDER_HISTORY)