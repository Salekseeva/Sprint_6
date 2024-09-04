import pytest
import allure
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import data, MAIN_URL, ORDER_URL


@pytest.mark.parametrize("order_button_locator", [
    MainPageLocators.ORDER_BUTTON_HEADER,
    MainPageLocators.ORDER_BUTTON_MIDDLE
])
@pytest.mark.parametrize("test_data", data)
def test_order_scooter(driver, order_button_locator, test_data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.open_page(MAIN_URL)

    with allure.step("Клик на кнопку заказа"):
        main_page.scroll_to_button(order_button_locator)  # Прокрутка к кнопке заказа
        main_page.click_element(order_button_locator)  # Клик по кнопке заказа


    WebDriverWait(driver, 10).until(EC.url_contains(ORDER_URL))
    assert ORDER_URL in driver.current_url, "Не произошло перенаправление на страницу оформления заказа"

    with allure.step("Заполнение формы заказа"):
        order_page.enter_name(test_data["name"])
        order_page.enter_surname(test_data["surname"])
        order_page.enter_address(test_data["address"])

        order_page.select_metro_station(test_data['metro'])
        order_page.enter_phone(test_data["phone"])
        order_page.click_next()

    with allure.step("Заполнение информации по заказу"):
        date = (datetime.now() + timedelta(days=2)).strftime("%d.%m.%Y")
        order_page.enter_rent_date(date)
        order_page.select_rent_duration(test_data["rent_duration"])
        order_page.select_scooter_color()
        order_page.enter_comment(test_data["comment"])
        order_page.submit_order()
        order_page.confirm_order()

    with allure.step("Подтверждение заказа"):
        assert order_page.is_order_confirmed, "Всплывающее окно подтверждения не появилось"
