import allure
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.main_functional_locators import MainFunctionalLocators
from data import urls


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_start_page(self):
        return self.navigate(urls.URL)

    @allure.step('Клик на ленту заказов')
    def click_feed_button(self):
        self.click_element(OrderFeedLocators.ORDER_FEED_BUTTON)
        self.wait_for_element_visible(OrderFeedLocators.ALL_ORDER_COUNTER)

    @allure.step('Получить номер первого заказа в ленте')
    def get_id_first_order_in_feed(self):
        return self.get_text(OrderFeedLocators.FIRST_ORDER_IN_FEED)

    @allure.step('Клик на заказ')
    def click_order_in_feeds(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER_IN_FEED)

    @allure.step('Получить id заказа')
    def get_id_in_order_details(self):
        return self.get_text(OrderFeedLocators.ID_IN_ORDER_DETAILS)

    @allure.step('Проверить появление окна с деталями заказа')
    def find_popup_order_detail(self):
        return self.find_element(OrderFeedLocators.ORDER_DETAIL)

    @allure.step('Получить id заказа в окне с деталями заказа')
    def get_order_id(self):
        return self.get_text(MainFunctionalLocators.ID_IN_POP_UP_ORDER)

    @allure.step('Закрыть окно с деталями заказа')
    def close_confirm_order_popup(self):
        self.click_element(MainFunctionalLocators.POP_UP_ORDER_CLOSE)

    @allure.step('Ожидание появления номера заказа в окне заказа')
    def wait_order_number(self):
        for _ in range(10):
            if self.get_text(MainFunctionalLocators.ID_IN_POP_UP_ORDER) == '9999':
                time.sleep(1)
            else:
                break

    @allure.step('Получение id заказа в окне заказа')
    def find_order_id_in_feed(self, order_number):
        locator = (By.XPATH, f"//p[contains(text(), '{order_number}')]")
        return self.find_element(locator)

    @allure.step('Получение количества заказов')
    def get_count(self, locator):
        return self.get_text(locator)

    @allure.step('Ожидание появления счетчика заказов')
    def wait_counter(self, locator):
        self.wait_for_element_visible(locator)

    @allure.step('Ожидание появления номера заказ в работе')
    def get_number_order_in_progress(self):
        time.sleep(5)
        return self.get_text(OrderFeedLocators.LAST_ORDER_IN_PROGRESS)[1:]
