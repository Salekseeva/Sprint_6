#order_page_locators.py

from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    ORDER_SERNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ORDER_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    ORDER_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    ORDER_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    ORDER_BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]')
    ORDER_DATE_FROM = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CLICK = (By.XPATH, '//div[text()="Про аренду"]')
    ORDER_HOW_LONG = (By.CLASS_NAME, "Dropdown-placeholder")
    ORDER_COLOR_BLACK = (By.XPATH, "//input[@id='black']/..")
    ORDER_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_FINISH_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") and (text() = "Заказать")]')
    ORDER_CONFIRM_BUTTON = (By.XPATH, '//button[text() = "Да"]')
    ORDER_POOPUP = (By.XPATH, '//div[text()="Заказ оформлен"]')
    YA_LOGO = (By.XPATH, '//*[@id = "stella_logo_3464--react"]')

    def __init__(self, driver):
        self.driver = driver  # Инициализировали его атрибуты