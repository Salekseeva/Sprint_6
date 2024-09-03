# tests/test_important_questions.py

import pytest
import allure
from selenium.webdriver.common.action_chains import ActionChains
from test_data import questions_and_answers, MAIN_URL
from pages.main_page import MainPage


@pytest.mark.parametrize("question_index, expected_answer", questions_and_answers)
def test_questions_and_answers(driver, question_index, expected_answer):
    main_page = MainPage(driver)
    main_page.open_page(MAIN_URL)

    with allure.step("Клик на Вопросы о важном"):
        question_element = main_page.get_question_element(question_index)
        driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        ActionChains(driver).move_to_element(question_element).perform()  # Прокрутка к элементу
        main_page.click_question(question_index)

    with allure.step("Получение ответа из Вопросы о важном"):
        answer_text = main_page.get_answer_text(question_index)

    with allure.step("Сравнение полученного ответа с ожидаемым ответом на Вопрос"):
        assert answer_text == expected_answer, f"Expected '{expected_answer}', but got '{answer_text}'"
