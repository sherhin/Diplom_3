import pytest
from selenium import webdriver

from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.authorization_page import AuthorizationPage
from pages.restore_page import RestorePage
from pages.account_page import AccountPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выберите браузер: chrome или firefox")

@pytest.fixture(scope="function")
def driver(request):
    """Создание вебдрайвер-клиента
    """
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается.")
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

@pytest.fixture(scope='function')
def account_page(driver):
    url_path = Urls.ACCOUNT_PAGE
    return AccountPage(driver, url_path)