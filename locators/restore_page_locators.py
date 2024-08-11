from selenium.webdriver.common.by import By

class RestorePageLocators:
    RESTORE_PASSWORD_TEXT = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    RESTORE_EMAIL_FIELD = [By.XPATH, '//input[@class="text input__textfield text_type_main-default"]']
    RESTORE_BUTTON = [By.XPATH, "//form//button[text()= 'Восстановить']"]
    CODE_INPUT = [By.XPATH, '//*[@class="input pr-6 pl-6 input_type_text input_size_default"]']
    RESTORE_PASSWORD_ACTIVE_INPUT = [By.XPATH,
                                     './/div[@class="input pr-6 pl-6 input_type_text input_size_default '
                                     'input_status_active"]']
    EYE = [By.XPATH, './/div[@class = "input__icon input__icon-action"]']
    FORGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")