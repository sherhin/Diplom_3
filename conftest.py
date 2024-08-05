import pytest
from selenium import webdriver

from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.authorization_page import AuthorizationPage
from pages.restore_page import RestorePage

@pytest.fixture(scope='function')
def driver():
    """Создание вебдрайвер-клиента
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def order_page(driver):
    url_path = Urls.ORDER_PAGE
    return OrderPage(driver, url_path)

@pytest.fixture(scope='function')
def authorization_page(driver):
    url_path = Urls.AUTHORIZATION_PAGE
    return AuthorizationPage(driver, url_path)

@pytest.fixture(scope='function')
def restore_page(driver):
    url_path = Urls.RESET_PASSWORD_PAGE
    return RestorePage(driver, url_path)