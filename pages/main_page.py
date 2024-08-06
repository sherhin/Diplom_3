from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Urls

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_to_constructor(self):
        self.open_page()
        self.click_to_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_to_order_page(self):
        self.open_page()
        self.click_to_element(MainPageLocators.ORDER_FEED)

    def click_to_account_page(self):
        self.open_page()
        self.click_to_element(MainPageLocators.ACCOUNT_LINK)


