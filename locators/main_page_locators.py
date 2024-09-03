# locators/main_page_locators.py

from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы кнопок заказа
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_MIDDLE = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')

    # Локаторы логотипов
    LOGO_SAMOKAT = (By.XPATH, '//img[contains(@alt, "Scooter")]')
    LOGO_YANDEX = (By.XPATH, '//img[contains(@alt, "Yandex")]')

    # Локаторы для раздела "Вопросы о важном"
    QUESTIONS = [(By.ID, f'accordion__heading-{i}') for i in range(8)]
    ANSWERS = [(By.XPATH, f'//*[@id="accordion__panel-{i}"]/p') for i in range(8)]