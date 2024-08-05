from data import Urls

class TestRestorePassword:

    def test_reset_password_page(self, restore_page):
        restore_page.open_page()
        url = restore_page.get_url()
        assert Urls.FORGOT_PASSWORD_PAGE in url

    def test_reset_password_form(self, restore_page):
        restore_page.open_page()
        restore_page.restore_password_button()
        restore_page.wait_reset_password_page()
        url = restore_page.get_url()
        assert Urls.RESET_PASSWORD_PAGE in url

    def test_show_password(self, restore_page):
        restore_page.open_page()
        restore_page.restore_password_button()
        restore_page.wait_reset_password_page()
        restore_page.click_show_password()
        password_field_active = restore_page.is_password_field_active()
        assert password_field_active
