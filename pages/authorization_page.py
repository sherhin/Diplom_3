from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import Urls

class AuthorizationPage(BasePage):

    def login(self, email, password):
        self.open_page()
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url_change(Urls.MAIN_PAGE)



