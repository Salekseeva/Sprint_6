# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """
    Инициализирует и возвращает экземпляр Firefox WebDriver.
    WebDriver закрывается после выполнения теста.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()
