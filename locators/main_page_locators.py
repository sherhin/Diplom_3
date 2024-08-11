from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_LINK = [By.XPATH, "//header//a[@href='/account']"]
    CONSTRUCTOR_LINK = [By.XPATH, "//nav//a[contains(@class, 'AppHeader') and @href='/']"]
    ORDER_FEED = [By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']"]
    ORDER_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]
    BUN_INGREDIENT = [By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']"]
    SAUCE_INGREDIENT = [By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa74']"]
    FILLED_INGREDIENT = [By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa78']"]
    DETAILS = [By.XPATH, ".//h2[@class= 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']"]
    CLOSE = [By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    POPUP = [By.XPATH, ".//div[@class = 'Modal_modal__contentBox__sCy8X pt-10 pb-15']"]
    MY_BURGER = [By.XPATH, "//span[@class = 'constructor-element__row']"]
    ORDER_PLACED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']"]
    INGREDIENT_COUNTER = [By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]']
