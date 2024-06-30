import allure
from pages.personal_account_page import PersonalAccountPage
from data import urls


class TestPersonalAccount:

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_personal_account_signin(self, driver, create_user, login_user):
        account_page = PersonalAccountPage(driver)
        account_page.to_personal_account()
        assert account_page.current_url() == urls.ACCOUNT_PROFILE

    @allure.title('Переход в раздел "История заказов"')
    def test_order_history(self, driver, create_user, login_user):
        account_page = PersonalAccountPage(driver)
        account_page.to_personal_account()
        account_page.order_history()
        assert account_page.current_url() == urls.ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, create_user, login_user):
        account_page = PersonalAccountPage(driver)
        account_page.to_personal_account()
        account_page.logout()
        assert account_page.current_url() == urls.LOGIN_URL
