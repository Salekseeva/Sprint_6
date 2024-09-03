# pages/main_page.py

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = MainPageLocators()

    def click_order_button_header(self):
        self.click_element(self.locators.ORDER_BUTTON_HEADER)

    def click_order_button_middle(self):
        self.click_element(self.locators.ORDER_BUTTON_MIDDLE)

    def click_scooter_logo(self):
        self.click_element(self.locators.LOGO_SAMOKAT)

    def click_yandex_logo(self):
        self.click_element(self.locators.LOGO_YANDEX)

    def get_question_element(self, index):
        question_locator = self.locators.QUESTIONS[index]
        return self.driver.find_element(*question_locator)

    def click_question(self, index):
        question_locator = self.locators.QUESTIONS[index]
        self.scroll_to_element(question_locator)  # Прокрутка к вопросу
        self.driver.find_element(*question_locator).click()

    def get_answer_text(self, index):
        answer_locator = self.locators.ANSWERS[index]
        return self.driver.find_element(*answer_locator).text
