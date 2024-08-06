import time

from helpers_api.conftest import api_client
from helpers_api.helpers_api import HelpersApi as help_api
class TestAccountPage:


    def test_logout(self, account_page, authorization_page, main_page, api_client):
        data = help_api.create_user_without_data(api_client)
        email = data['email']
        password = data['password']
        authorization_page.login(email, password)
        main_page.click_to_account_page()
        account_page.logout()
        url = account_page.get_url()
        assert 'login' in url


    def test_move_to_order_history(self, account_page, authorization_page, main_page, api_client):
        data = help_api.create_user_without_data(api_client)
        email = data['email']
        password = data['password']
        authorization_page.login(email, password)
        main_page.click_to_account_page()
        account_page.move_to_order_history()
        url = account_page.get_url()
        assert 'order-history' in url
