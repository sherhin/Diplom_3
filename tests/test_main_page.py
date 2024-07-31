
class TestMainPage:

    def test_click_to_order_page(self, main_page):
        main_page.click_to_order_page()
        current_page = main_page.get_url()
        assert 'feed' in current_page