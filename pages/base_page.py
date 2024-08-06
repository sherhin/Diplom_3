import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Urls


class BasePage:
    def __init__(self, driver, url_path=''):
        self.driver = driver
        url = Urls.MAIN_PAGE
        self.url = url + url_path

    @allure.step('Открыть страницу')
    def open_page(self):
        url = self.url
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Найти элемент')
    def find_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть по элементу')
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Сформировать локатор')
    def format_locators(self, locator, id):
        method, locator = locator
        format_locator = locator.format(id)

        return method, format_locator

    @allure.step('Отправить текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Сменить вкладку')
    def switch_tab(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ждем смены url')
    def wait_for_url_change(self, url, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url == url)
        return self.driver.current_url

