import allure

from pages.base_page import BasePage
from locators.main_functional_locators import MainFunctionalLocators
from data import urls


class MainFunctionalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_start_page(self):
        return self.navigate(urls.URL)

    @allure.step('Клик на ленту заказов')
    def click_feed_button(self):
        self.click_element_script(MainFunctionalLocators.ORDER_FEED_BUTTON, 10)
        self.wait_for_element_visible(MainFunctionalLocators.ORDER_FEED_HEADER,10)

    @allure.step('Клик на конструктор')
    def click_constructor_button(self):
        self.click_element_script(MainFunctionalLocators.CONSTRUCTOR_BUTTON, 10)
        self.wait_for_element_visible(MainFunctionalLocators.MAKE_BURGER_HEADER, 10)

    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.click_element_script(MainFunctionalLocators.INGREDIENT, 10)
        self.wait_for_element_visible(MainFunctionalLocators.POP_UP_HEADER, 10)

    @allure.step('Поиск заголовка окна с деталями ингридиента')
    def find_head_popup(self):
        return self.find_element(MainFunctionalLocators.POP_UP_HEADER, 10)

    @allure.step('Клик на крестик')
    def click_popup_close(self):
        self.click_element_script(MainFunctionalLocators.POP_UP_CLOSE, 10)

    @allure.step('Поиск окна с деталями ингридиента')
    def find_popup(self):
        return self.find_element(MainFunctionalLocators.MODAL_SECTION, 10)

    @allure.step('Перемещение ингридиента')
    def replace_ingredient(self):
        ingredient = self.find_element(MainFunctionalLocators.INGREDIENT, 10)
        basket = self.find_element(MainFunctionalLocators.BASKER_AREA, 10)
        self.replace_element(ingredient, basket)

    @allure.step('Получение количества ингредиентов')
    def get_count(self):
        self.wait_for_element_visible(MainFunctionalLocators.INGREDIENT_COUNTER, 10)
        return self.get_text(MainFunctionalLocators.INGREDIENT_COUNTER, 10)

    @allure.step('Клик на Оформить заказ')
    def click_place_order(self):
        self.click_element(MainFunctionalLocators.PLACE_ORDER_BUTTON, 10)
        self.wait_for_element_visible(MainFunctionalLocators.POP_UP_ORDER, 10)

    @allure.step('Поиск окна с подтверждением заказа')
    def find_popup_confirm_order(self):
        return self.find_element(MainFunctionalLocators.POP_UP_ORDER, 10)

    @allure.step('Получить адрес текущей страницы')
    def current_url(self):
        return self.get_current_url()

    def make_order(self):
        self.click_constructor_button()
        self.replace_ingredient()
        self.click_place_order()
