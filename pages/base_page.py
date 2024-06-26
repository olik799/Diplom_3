from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def scroll_page(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def get_current_url(self):
        return self.driver.current_url

    def get_value(self, locator, value):
        return self.find_element(locator).get_attribute(value)

    def replace_element(self, element_locator, place_locator):
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element_locator, place_locator).perform()
