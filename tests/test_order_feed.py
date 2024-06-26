import allure
import pytest

from pages.main_functional_page import MainFunctionalPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage

from locators.order_feed_locators import OrderFeedLocators


class TestMainFunctional:

    @allure.title('Клик на заказ в «Ленте заказов» открывает всплывающее окно с деталями')
    def test_order_detail(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_start_page()
        order_feed.click_feed_button()
        id_first_order_in_feed = order_feed.get_id_first_order_in_feed()
        order_feed.click_order_in_feeds()
        id_in_order_detail = order_feed.get_id_in_order_details()
        assert order_feed.find_popup_order_detail() and id_first_order_in_feed == id_in_order_detail

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_in_order_feed(self, driver):
        account_page = PersonalAccountPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        main_functional = MainFunctionalPage(driver)
        main_functional.click_constructor_button()
        main_functional.replace_ingredient()
        main_functional.click_place_order()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_order_number()
        order_number = '#0' + order_feed.get_order_id()
        order_feed.close_confirm_order_popup()
        order_feed.click_feed_button()
        assert order_feed.find_order_id_in_feed(order_number)
        account_page.delete_user(user_data[1])

    @allure.title('При создании нового заказа счётчик {counter_type} увеличиваются')
    @pytest.mark.parametrize("counter_type, locator", [("Выполнено за всё время", OrderFeedLocators.ALL_ORDER_COUNTER),
                                                       ("Выполнено за сегодня", OrderFeedLocators.DAY_ORDER_COUNTER)])
    def test_counter(self, driver, counter_type, locator):
        account_page = PersonalAccountPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        order_feed = OrderFeedPage(driver)
        order_feed.click_feed_button()
        count_current = order_feed.get_count(locator)
        main_functional = MainFunctionalPage(driver)
        main_functional.click_constructor_button()
        main_functional.replace_ingredient()
        main_functional.click_place_order()
        order_feed.wait_order_number()
        order_feed.close_confirm_order_popup()
        order_feed.click_feed_button()
        order_feed.wait_counter(locator)
        assert order_feed.get_count(locator) > count_current
        account_page.delete_user(user_data[1])

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_user_order_in_progress(self, driver):
        account_page = PersonalAccountPage(driver)
        user_data = account_page.create_user()
        account_page.signup(user_data[0])
        main_functional = MainFunctionalPage(driver)
        main_functional.click_constructor_button()
        main_functional.replace_ingredient()
        main_functional.click_place_order()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_order_number()
        order_number = order_feed.get_order_id()
        order_feed.close_confirm_order_popup()
        order_feed.click_feed_button()
        assert order_feed.get_number_order_in_progress() == order_number
        account_page.delete_user(user_data[1])
