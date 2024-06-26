from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    """Форма регистрации"""

    NAME_FIELD = By.XPATH, "//label[text()='Имя']/following::input"  # форма регистрации поле Имя
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following::input"  # форма регистрации поле email
    PASSWORD_FIELD = By.NAME, "Пароль"  # форма регистрации поле Пароль
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"  # форма регистрации кнопка Зарегистрироваться
    INPUT_HEADER = By.XPATH, "//h2[text()='Вход']"
    INPUT_BUTTON = By.XPATH, "//button[text()='Войти']"  # кнопка Войти - форма ввода email и пароль
    MAKE_BURGER_HEADER = By.XPATH, "//h1[text()='Соберите бургер']"  # Заголовок Собери бургер

    """Личный кабинет пользователя"""

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"  # кнопка Личный Кабинет
    PROFILE_HEADER = By.XPATH, "//a[text()='Профиль']"
    ORDER_HISTORY = By.XPATH, "//a[text()='История заказов']"
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
