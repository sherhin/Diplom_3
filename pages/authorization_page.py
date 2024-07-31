import time

from pages.base_page import BasePage
from locators.restore_page_locators import RestorePage
from data import Urls


class AuthorizationPage(BasePage):

    def move_to_reset_page(self):
        self.open_page()
        self.click_to_element(RestorePage.FORGOT_PASSWORD)

    def restore_password_button(self):
        self.move_to_reset_page()
        self.add_text_to_element(RestorePage.RESTORE_EMAIL_FIELD, 'email@email.ru')
        self.click_to_element(RestorePage.RESTORE_BUTTON)

    def wait_reset_password_page(self):
        self.wait_for_url_change(url=Urls.MAIN_PAGE+Urls.RESET_PASSWORD_PAGE)