import allure
from pages.base_page import BasePage
from locators.recover_password_locators import RecoverPasswordLocators
from data import urls, generate_user


class RecoverPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Загрузка страницы входа в личный кабинет')
    def load_page(self):
        self.navigate(urls.LOGIN_URL)
        self.wait_for_element_visible(RecoverPasswordLocators.RECOVER_PASSWORD_BUTTON, 10)

    @allure.step('Кликнуть на "Восстановить пароль"')
    def click_recover_password(self):
        self.click_element(RecoverPasswordLocators.RECOVER_PASSWORD_BUTTON, 10)
        self.wait_for_element_visible(RecoverPasswordLocators.RECOVER_HEADER, 10)

    @allure.step('Получить адрес текущей страницы')
    def current_url(self):
        return self.get_current_url()

    @allure.step('Загрузка страницы восстановления пароля')
    def load_recover_page(self):
        self.navigate(urls.FORGOT_PASSWORD)
        self.wait_for_element_visible(RecoverPasswordLocators.RECOVER_HEADER, 10)

    @allure.step('Заполнить поле "email"')
    def set_email(self, email):
        self.enter_text(RecoverPasswordLocators.EMAIL_FIELD_RECOVER, 10, email)

    @allure.step('Получение значения в поле "email"')
    def get_value_field(self):
        return self.get_value(RecoverPasswordLocators.EMAIL_FIELD_RECOVER, 10, 'value')

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recover_button(self):
        self.click_element_script(RecoverPasswordLocators.RECOVER_BUTTON, 10)
        self.wait_for_element_visible(RecoverPasswordLocators.SAVE_BUTTON, 10)

    @allure.step('Клик по кнопке "Скрыть/Показать"')
    def click_eye_button(self):
        self.click_element_script(RecoverPasswordLocators.EYE_BUTTON, 10)

    @allure.step('Получение значения в поле "Пароль"')
    def get_class_password_field(self):
        return self.get_value(RecoverPasswordLocators.PASSWORD_FIELD, 10, 'class')
