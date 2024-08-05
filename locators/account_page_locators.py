from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_IN_ACCOUNT = [By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']"]
    ORDERS_HISTORY = [By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']"]
    ORDER_HISTORY_INACTIVE = [By.XPATH,
                              "//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive']"]
    ORDER_HISTORY_ACTIVE = [By.XPATH,
                            ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]
    EXIT_BUTTON = [By.XPATH, ".//button[contains(@class, 'Account_button')][text()='Выход']"]