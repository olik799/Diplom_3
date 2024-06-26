import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == 'firefox':
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
