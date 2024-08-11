from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = [By.XPATH, "//form//label[text() = 'Email']/../input"]
    PASSWORD_FIELD = [By.XPATH, "//form//input[@type='password']"]
    LOGIN_BUTTON = [By.XPATH, "//form//button"]
    RESTORE_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")