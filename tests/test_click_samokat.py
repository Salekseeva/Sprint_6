# tests/test_click_samokat.py
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from test_data import MAIN_URL, ORDER_URL


@allure.description("Клик на Логотип Самокат")
def test_logo_redirect_samokat(driver):
    driver.get(ORDER_URL)
    with allure.step("Проверка перехода по логотипу Самоката"):
        driver.find_element(*MainPageLocators.LOGO_SAMOKAT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert MAIN_URL == driver.current_url, "Не произошло перенаправление на главную страницу 'Самоката'"