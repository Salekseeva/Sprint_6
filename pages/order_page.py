# order_page.py
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def enter_name(self, name):
        self.enter_text(OrderPageLocators.ORDER_NAME, name)

    def enter_surname(self, surname):
        self.enter_text(OrderPageLocators.ORDER_SERNAME, surname)

    def enter_address(self, address):
        self.enter_text(OrderPageLocators.ORDER_ADDRESS, address)

    def select_metro_station(self, station_name):
        self.click_element(OrderPageLocators.ORDER_METRO)
        metro_locator = (By.XPATH, f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='{station_name}']")
        self.click_element(metro_locator)

    def enter_phone(self, phone):
        self.enter_text(OrderPageLocators.ORDER_PHONE, phone)

    def click_next(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_NEXT)

    def enter_rent_date(self, date):
        self.enter_text(OrderPageLocators.ORDER_DATE_FROM, date)

    def select_rent_duration(self, duration):
        self.click_element(OrderPageLocators.ORDER_HOW_LONG)
        duration_locator = (By.XPATH, f"//div[@role='option' and text()='{duration}']")
        self.click_element(duration_locator)

    def select_scooter_color(self):
        self.click_element(OrderPageLocators.ORDER_COLOR_BLACK)

    def enter_comment(self, comment):
        self.enter_text(OrderPageLocators.ORDER_COMMENT, comment)

    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_FINISH_BUTTON)

    def confirm_order(self):
        self.click_element(OrderPageLocators.ORDER_CONFIRM_BUTTON)

    def is_order_confirmed(self):
        return self.wait_and_find_element(OrderPageLocators.ORDER_POOPUP).is_displayed()
