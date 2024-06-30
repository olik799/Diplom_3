from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def scroll_page(self, locator, timeout):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator, timeout):
        self.wait_for_element_visible(locator, timeout)
        self.find_element(locator, timeout).click()

    def get_text(self, locator, timeout):
        return self.find_element(locator, timeout).text

    def enter_text(self, locator, timeout, text):
        self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_loading_element(self, locator, timeout):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(locator)

    def get_current_url(self):
        return self.driver.current_url

    def get_value(self, locator, timeout, value):
        return self.find_element(locator, timeout).get_attribute(value)

    def replace_element(self, element_locator, place_locator):
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element_locator, place_locator).perform()

    def click_element_script(self, locator, timeout):
        element = self.wait_for_element_visible(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)