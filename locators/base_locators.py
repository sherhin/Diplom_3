from selenium.webdriver.common.by import By

class BasePageLocators:
    lk_button = (By.XPATH, "//a[.='Личный Кабинет']")  # Личный кабинет
    order_page = (By.XPATH, "//a[.='Лента Заказов']")
    registration_button = (By.XPATH, '//a[@href="/register"]')  # Регистрация
    email_field = (By.XPATH, './/label[text() = "Email"]/../input')  # Поле ввода email
    password_field = (By.XPATH, './/label[text() = "Пароль"]/../input')  # Поле ввода пароля
    name_field = (By.XPATH, './/label[text() = "Имя"]/../input')  # Поле ввода логина
    registry_button = (By.XPATH, '//button[.="Зарегистрироваться"]')  # Кнопка Зарегистрироваться
    enter_button = (By.XPATH, '//main//button')  # Кнопка Войти
    account_button = (By.XPATH, '//button[.="Войти в аккаунт"]')  # Кнопка Войти в аккаунт
    logout_button = (By.XPATH, '//button[.="Выход"]')  # Кнопка Выход
    forgot_password_auth_button = (By.XPATH, '//a[@href="/login"]')  # Кнопка восстановления пароля
    constructor = (By.XPATH, '//p[.="Конструктор"]')  # Конструктор
    sauces = (By.XPATH, '//div[.="Соусы"]')  # Раздел соусов
    buns = (By.XPATH, '//div[.="Булки"]')  # Раздел булок
    ingredients = (By.XPATH, '//div[.="Начинки"]')  # Раздел начинок
    logo_button = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")  # Логотип
    input_error = (By.CLASS_NAME, "input__error")
    order_id = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    ingredient = (By.XPATH, '//a[@href="/feed{}"]')
    number_order_from_feed = [By.XPATH, "//p[@class = 'text text_type_digits-default mb-10 mt-5']"]
    contain = [By.XPATH, "//p[@class = 'text text_type_main-medium mb-8']"]
    containing_elements = [By.XPATH, "//p[@class = 'undefined text text_type_main-default'][1]"]
    order_container = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"]
    restore_password = (By.XPATH, ".//a[@href='/forgot-password']")