from selenium.webdriver.common.by import By


class MainFunctionalLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    MAKE_BURGER_HEADER = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDER_FEED_HEADER = By.XPATH, "//h1[text()='Лента заказов']"

    INGREDIENT = By.XPATH, "//a[contains(@href, '/ingredient/')]"
    INGREDIENT_COUNTER = By.XPATH, "//p[contains(@class, 'counter__num')]"
    BASKER_AREA = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    """pop_up_ingredient"""

    POP_UP_HEADER = By.XPATH, "//h2[text()='Детали ингредиента']"
    POP_UP_CLOSE = By.XPATH, "//button[contains(@class, 'modal__close')]"
    MODAL_SECTION = By.XPATH, "//section[contains(@class, 'Modal_modal')]"

    """pop_up_order"""

    POP_UP_ORDER = By.XPATH, "//p[text()='идентификатор заказа']"
    ID_IN_POP_UP_ORDER = By.XPATH, "//h2[contains(@class, 'modal__title')]"
    POP_UP_ORDER_CLOSE = By.XPATH, "//button[contains(@class, 'modal__close')]"
