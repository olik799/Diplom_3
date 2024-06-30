from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    FIRST_ORDER_IN_FEED = By.XPATH, "//li[contains(@class, 'OrderHistory')]//p[contains(@class, 'digits-default')]"
    LAST_ORDER_IN_PROGRESS = By.XPATH, "//ul[contains(@class,'orderListReady')]/li[1]"

    """Поп-ап детали заказа"""

    ORDER_DETAIL = By.XPATH, "//div[contains(@class, 'modal__container')]"
    ID_IN_ORDER_DETAILS = By.XPATH, "//div[contains(@class,'Modal_orderBox')]/p"

    """Счетчики заказов"""

    DAY_ORDER_COUNTER = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ALL_ORDER_COUNTER = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
