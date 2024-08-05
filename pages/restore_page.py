from pages.base_page import BasePage
from locators.restore_page_locators import RestorePageLocators
from data import Urls


class RestorePage(BasePage):

    def restore_password_button(self):
        self.add_text_to_element(RestorePageLocators.RESTORE_EMAIL_FIELD, 'email@email.ru')
        self.click_to_element(RestorePageLocators.RESTORE_BUTTON)

    def wait_reset_password_page(self):
        self.wait_for_url_change(url=Urls.MAIN_PAGE+Urls.RESET_PASSWORD_PAGE)

    def click_show_password(self):
        self.click_to_element(RestorePageLocators.EYE)

    def is_password_field_active(self):
        password_field = self.find_element_with_wait(RestorePageLocators.RESTORE_PASSWORD_ACTIVE_INPUT)
        return password_field