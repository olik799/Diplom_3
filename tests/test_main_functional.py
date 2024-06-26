import allure
from pages.main_functional_page import MainFunctionalPage
from pages.personal_account_page import PersonalAccountPage
from data import urls


class TestMainFunctional:

    @allure.title('Переход в ленту заказов')
    def test_to_constructor(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.open_start_page()
        main_functional.click_feed_button()
        assert main_functional.current_url() == urls.FEED

    @allure.title('Переход в конструктор')
    def test_to_constructor(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.open_start_page()
        main_functional.click_feed_button()
        main_functional.click_constructor_button()
        assert main_functional.current_url() == urls.URL

    @allure.title('Клик на ингридиент открывает окно с деталями')
    def test_open_popup(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.open_start_page()
        main_functional.click_ingredient()

        assert 'modal__title' in main_functional.find_head_popup().get_attribute('class')

    @allure.title('Клик на крестик закрывает окно с деталями')
    def test_open_popup(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.open_start_page()
        main_functional.click_ingredient()
        main_functional.click_popup_close()
        assert 'opened' not in main_functional.find_popup().get_attribute('class')

    @allure.title('Добавление ингредиента в заказ увеличивает счетчиу этого ингредиента')
    def test_adding_ingredient_increases_counter(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.open_start_page()
        current_counter = int(main_functional.get_count())
        main_functional.replace_ingredient()
        add_counter = int(main_functional.get_count())
        assert current_counter < add_counter

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_user_make_order(self, driver):
        account_page = PersonalAccountPage(driver)
        main_functional = MainFunctionalPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        main_functional.click_constructor_button()
        main_functional.replace_ingredient()
        main_functional.click_place_order()
        assert main_functional.find_popup_confirm_order()
        account_page.delete_user(user_data[1])
