import pytest
import allure
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from test_data import data, MAIN_URL, ORDER_URL


@pytest.mark.parametrize("test_data", data)
def test_order_scooter_header_button(driver, test_data):
    order_page = OrderPage(driver)
    order_page.open_page(MAIN_URL)

    with allure.step("Клик на кнопку заказа в шапке страницы"):
        driver.find_element(*MainPageLocators.ORDER_BUTTON_HEADER).click()

    WebDriverWait(driver, 10).until(EC.url_contains(ORDER_URL))
    assert ORDER_URL in driver.current_url, "Не произошло перенаправление на страницу оформления заказа"

    with allure.step("Заполнение формы заказа"):
        driver.find_element(*OrderPageLocators.ORDER_NAME).send_keys(test_data["name"])
        driver.find_element(*OrderPageLocators.ORDER_SERNAME).send_keys(test_data["surname"])
        driver.find_element(*OrderPageLocators.ORDER_ADDRESS).send_keys(test_data["address"])

        driver.find_element(*OrderPageLocators.ORDER_METRO).click()
        metro_locator = f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='{test_data['metro']}']"
        driver.find_element(By.XPATH, metro_locator).click()

        phone = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.ORDER_PHONE))
        phone.click()
        phone.send_keys(test_data["phone"])
        driver.find_element(*OrderPageLocators.ORDER_BUTTON_NEXT).click()

    with allure.step("Заполнение информации по заказу"):
        date = (datetime.now() + timedelta(days=2)).strftime("%d.%m.%Y")
        driver.find_element(*OrderPageLocators.ORDER_DATE_FROM).send_keys(date)
        driver.find_element(*OrderPageLocators.CLICK).click()

        driver.find_element(*OrderPageLocators.ORDER_HOW_LONG).click()
        rent_duration_locator = f"//div[text()='{test_data['rent_duration']}']"
        driver.find_element(By.XPATH, rent_duration_locator).click()
        driver.find_element(*OrderPageLocators.ORDER_COLOR_BLACK).click()
        driver.find_element(*OrderPageLocators.ORDER_COMMENT).send_keys(test_data["comment"])
        driver.find_element(*OrderPageLocators.ORDER_FINISH_BUTTON).click()
        driver.find_element(*OrderPageLocators.ORDER_CONFIRM_BUTTON).click()

    with allure.step("Подтверждение заказа"):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_POOPUP))
        assert driver.find_element(
            *OrderPageLocators.ORDER_POOPUP).is_displayed(), "Всплывающее окно подтверждения не появилось"
        driver.find_element(*OrderPageLocators.ORDER_VIEW_STATUS_BUTTON).click()
