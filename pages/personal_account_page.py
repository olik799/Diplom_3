import allure
import requests

from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_functional_locators import MainFunctionalLocators
from data import urls, generate_user


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Регистрация пользователя')
    def create_user(self):
        payload = generate_user.generate_data_for_new_user()
        response = requests.post(urls.EP_CREATE_USER, data=payload)
        auth = response.json()["accessToken"]
        return payload, auth

    @allure.step('Авторизация на сайте')
    def signup(self, email, password):
        self.enter_text(PersonalAccountLocators.EMAIL_FIELD, 10, email)
        self.enter_text(PersonalAccountLocators.PASSWORD_FIELD, 10, password)
        self.click_element(PersonalAccountLocators.INPUT_BUTTON, 10)
        self.wait_for_element_visible(MainFunctionalLocators.PLACE_ORDER_BUTTON, 10)

    @allure.step('Вход в личный кабинет')
    def personal_account(self):
        self.click_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON, 10)
        self.wait_for_element_visible(PersonalAccountLocators.INPUT_HEADER, 10)

    @allure.step('Переходд в личный кабинет')
    def to_personal_account(self):
        self.click_element_script(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON, 10)
        self.wait_for_element_visible(PersonalAccountLocators.PROFILE_HEADER, 10)

    @allure.step('Переход в историю заказов')
    def order_history(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY, 10)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.click_element(PersonalAccountLocators.EXIT_BUTTON, 10)
        self.wait_for_element_visible(PersonalAccountLocators.INPUT_HEADER, 10)

    @allure.step('Получить адрес текущей страницы')
    def current_url(self):
        return self.get_current_url()

    @allure.step('Удалить пользователя')
    def delete_user(self, auth):
        requests.delete(urls.EP_DELETE_OR_UPDATE_USER, headers={"Authorization": auth})
