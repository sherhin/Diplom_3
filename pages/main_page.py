from pages.base_page import BasePage
from locators.base_locators import BasePageLocators

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_to_constructor(self):
        self.click_to_element(BasePageLocators.constructor)

    def click_to_order_page(self):
        self.open_page()
        self.click_to_element(BasePageLocators.order_page)
