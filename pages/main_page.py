# pages/main_page.py

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = MainPageLocators()

    def scroll_to_button(self, locator):
        """Прокрутка к кнопке заказа"""
        self.scroll_to_element(locator)

    def click_order_button_header(self):
        self.scroll_to_button(self.locators.ORDER_BUTTON_HEADER)  # Прокрутка к кнопке
        self.click_element(self.locators.ORDER_BUTTON_HEADER)

    def click_order_button_middle(self):
        self.scroll_to_button(self.locators.ORDER_BUTTON_MIDDLE)  # Прокрутка к кнопке
        self.click_element(self.locators.ORDER_BUTTON_MIDDLE)

    def click_scooter_logo(self):
        self.click_element(self.locators.LOGO_SAMOKAT)

    def click_yandex_logo(self):
        self.click_element(self.locators.LOGO_YANDEX)

    def scroll_to_question(self, index):    # Добавлено
        question_locator = self.locators.QUESTIONS[index]
        self.scroll_to_element(question_locator)

    def click_question(self, index):
        question_locator = self.locators.QUESTIONS[index]
        self.click_element(question_locator) # Исправлено

    def get_answer_text(self, index):
        answer_locator = self.locators.ANSWERS[index]
        return self.wait_and_find_element(answer_locator).text # Исправлено, убрала "driver"
