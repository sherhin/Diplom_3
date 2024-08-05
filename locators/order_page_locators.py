from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER = [By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6'][1]"]
    NUMBER_ORDER_FROM_FEED = [By.XPATH, "//p[@class = 'text text_type_digits-default mb-10 mt-5']"]
    CONTAIN = [By.XPATH, "//p[@class = 'text text_type_main-medium mb-8']"]
    CONTAINING_ELEMENTS = [By.XPATH, "//p[@class = 'undefined text text_type_main-default'][1]"]
    STATUS = [By.XPATH, "//p[@class = 'undefined text text_type_main-default mb-15']"]
    ORDER_IN_ORDER_FEED = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    COMPLETED_ORDERS_TODAY_BEFORE = [By.XPATH, ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p"]
    LABEL_ALL_ORDERS_ARE_READY = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]"
                                            "/li[text()='Все текущие заказы готовы!']"]
    ORDER_LIST = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{}']"]