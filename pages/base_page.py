# pages/base_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(text)

    def open_page(self, url):
        self.driver.get(url)

    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
