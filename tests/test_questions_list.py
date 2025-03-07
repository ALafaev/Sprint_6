import allure
import pytest
from ..pages.main_page import MainPage
from data import EXPECTED_ANSWERS

class TestQuestionsList:

    @allure.title('Тест на соответствие текста ответа на вопрос о стоимости и способах оплаты (вопрос №1)')
    @allure.description('Кликаем на вопрос "Сколько это стоит? И как оплатить?", сверяем текст ответа с ОР')
    @pytest.mark.parametrize('question_id',range(8))
    def test_click_to_question_button_shows_answer(self, driver, question_id):
        main_page = MainPage(driver)
        main_page.scroll_to_question(question_id)
        main_page.click_to_question_button(question_id)
        main_page.check_answer_is_visible(question_id)
        actual_answer_text = main_page.get_answer_text(question_id)
        expected_answer_text = EXPECTED_ANSWERS[question_id]

        assert actual_answer_text == expected_answer_text, "Текст ответа не соответствует ОР"
