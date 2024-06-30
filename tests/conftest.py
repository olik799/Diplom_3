import pytest
import requests
from selenium import webdriver
from data.generate_user import generate_data_for_new_user
from pages.personal_account_page import PersonalAccountPage
from data import urls


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(urls.URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(urls.URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    payload = generate_data_for_new_user()
    response = requests.post(urls.EP_CREATE_USER, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    header = {'Authorization': token}
    requests.delete(urls.EP_DELETE_OR_UPDATE_USER, headers=header)


@pytest.fixture
def login_user(driver, create_user):
    user_data = create_user[0]
    account_page = PersonalAccountPage(driver)
    account_page.personal_account()
    account_page.signup(user_data['email'], user_data['password'])
