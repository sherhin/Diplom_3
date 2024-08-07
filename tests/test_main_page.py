import pytest

class TestMainPage:

    def test_click_to_order_page(self, main_page):
        main_page.click_to_order_page()
        current_page = main_page.get_url()
        assert 'feed' in current_page

    def test_click_to_account_page(self, main_page):
        main_page.click_to_account_page()
        current_page = main_page.get_url()
        assert 'login' in current_page

    @pytest.mark.parametrize('ingredient', ['bun', 'sauce', 'filled'])
    def test_click_ingredient(self, main_page, ingredient):
        main_page.click_to_ingredient(ingredient)
        popup = main_page.check_popup()
        assert popup == ('Детали ингредиента')

    @pytest.mark.parametrize('ingredient', ['bun', 'sauce', 'filled'])
    def test_close_popup(self, main_page, ingredient):
        main_page.click_to_ingredient(ingredient)
        popup = main_page.close_popup()
        assert not popup

