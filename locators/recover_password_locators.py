from selenium.webdriver.common.by import By


class RecoverPasswordLocators:
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[text()='Восстановить пароль']"
    EMAIL_FIELD_RECOVER = By.XPATH, "//label[text()='Email']/following::input"
    RECOVER_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    INPUT_BUTTON = By.XPATH, "//a[text()='Войти']"
    RECOVER_HEADER = By.XPATH, "//h2[text()='Восстановление пароля']"
    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"
    EYE_BUTTON = By.XPATH, "//*[@class='input__icon input__icon-action']"
    PASSWORD_FIELD = By.XPATH, "//label[text()='Пароль']"
