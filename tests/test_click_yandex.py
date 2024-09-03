# tests/test_click_yandex.py
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from test_data import ORDER_URL, DZEN_URL


@allure.description("Клик на Логотип Яндекс")
def test_logo_redirect_yandex(driver):
    driver.get(ORDER_URL)
    with allure.step("Проверка перехода по логотипу Яндекса"):
        driver.find_element(*MainPageLocators.LOGO_YANDEX).click()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.url_to_be(DZEN_URL))
        assert DZEN_URL == driver.current_url, "Не произошло перенаправление на главную страницу Дзена"