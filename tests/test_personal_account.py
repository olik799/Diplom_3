import allure
from pages.personal_account_page import PersonalAccountPage
from data import urls


class TestPersonalAccount:

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_personal_account_signin(self, driver):
        account_page = PersonalAccountPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        account_page.personal_account()
        assert account_page.current_url() == urls.ACCOUNT_PROFILE
        account_page.delete_user(user_data[1])

    @allure.title('Переход в раздел "История заказов"')
    def test_order_history(self, driver):
        account_page = PersonalAccountPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        account_page.personal_account()
        account_page.order_history()
        assert account_page.current_url() == urls.ORDER_HISTORY
        account_page.delete_user(user_data[1])

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver):
        account_page = PersonalAccountPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        account_page.personal_account()
        account_page.logout()
        assert account_page.current_url() == urls.LOGIN_URL
        account_page.delete_user(user_data[1])
