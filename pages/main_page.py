import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

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

    def click_to_ingredient(self, ingredient):
        self.open_page()
        if ingredient == 'bun':
            self.click_to_element(MainPageLocators.BUN_INGREDIENT)
        elif ingredient == 'sauce':
            self.click_to_element(MainPageLocators.SAUCE_INGREDIENT)
        else:
            self.click_to_element(MainPageLocators.FILLED_INGREDIENT)

    def check_count(self):
        ingredient_count = self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
        return ingredient_count

    def move_ingredient(self):
        self.open_page()
        ingredient = self.find_element_with_wait(MainPageLocators.BUN_INGREDIENT)
        burger_place = self.find_element_with_wait(MainPageLocators.MY_BURGER)
        self.drag_and_drop(ingredient, burger_place)

    def check_popup(self):
        popup = self.get_text_from_element(MainPageLocators.DETAILS)
        return popup

    def close_popup(self):
        self.click_to_element(MainPageLocators.CLOSE)
        popup = self.element_not_exists(MainPageLocators.POPUP)
        return popup
