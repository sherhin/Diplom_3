from data import Urls
class TestRestorePassword:

    def test_reset_password_page(self, authorization_page):
        authorization_page.move_to_reset_page()
        url = authorization_page.get_url()
        assert Urls.FORGOT_PASSWORD_PAGE in url

    def test_reset_password_form(self, authorization_page):
        authorization_page.restore_password_button()
        authorization_page.wait_reset_password_page()
        url = authorization_page.get_url()
        assert Urls.RESET_PASSWORD_PAGE in url