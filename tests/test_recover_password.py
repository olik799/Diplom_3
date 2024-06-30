import allure
from pages.recover_password_page import RecoverPasswordPage
from data import urls, generate_user


class TestRecoverPassword:

    @allure.title('Переход на страницу восстановления пароля')
    def test_redirect_recovery_password_page(self, driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.load_page()
        recover_page.click_recover_password()
        assert recover_page.current_url() == urls.FORGOT_PASSWORD

    @allure.title('Ввод почты')
    def test_set_email(self, driver):
        user_data = generate_user.generate_data_for_new_user()
        recover_page = RecoverPasswordPage(driver)
        recover_page.load_recover_page()
        recover_page.set_email(user_data.get('email'))
        assert recover_page.get_value_field() == user_data.get('email')

    @allure.title('Клик по кнопке "Восстановить"')
    def test_click_recover_button(self, driver):
        user_data = generate_user.generate_data_for_new_user()
        recover_page = RecoverPasswordPage(driver)
        recover_page.load_recover_page()
        recover_page.set_email(user_data.get('email'))
        recover_page.click_recover_button()
        assert recover_page.current_url() == urls.RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть')
    def test_click_eye_button(self, driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.load_recover_page()
        recover_page.click_recover_button()
        recover_page.click_eye_button()
        assert 'placeholder-focused' in recover_page.get_class_password_field()
