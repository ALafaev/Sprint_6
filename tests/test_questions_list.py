import allure
from ..pages.main_page import MainPage
from data import ExpectedAnswers

class TestQuestionsList:

    @allure.title('Тест на соответствие текста ответа на вопрос о стоимости и способах оплаты (вопрос №1)')
    @allure.description('Кликаем на вопрос "Сколько это стоит? И как оплатить?", сверяем текст ответа с ОР')
    def test_price_and_payment_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_prise_and_payment_question()
        main_page.click_to_price_and_payment_question_button()
        main_page.check_price_and_payment_answer_is_visible()
        actual_answer_text = main_page.get_price_and_payment_answer_text()
        expected_answer_text = ExpectedAnswers.PRICE_AND_PAYMENT

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о заказе нескольких самокатов (вопрос №2)')
    @allure.description('Кликаем на вопрос "Хочу сразу несколько самокатов! Так можно?", сверяем текст ответа с ОР')
    def test_few_scooters_rent_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_few_scooters_rent_question()
        main_page.click_to_few_scooters_rent_question_button()
        main_page.check_few_scooters_rent_answer_is_visible()
        actual_answer_text = main_page.get_few_scooters_rent_answer_text()
        expected_answer_text = ExpectedAnswers.FEW_SCOOTERS_RENT

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о времени аренды (вопрос №3)')
    @allure.description('Кликаем на вопрос "Как рассчитывается время аренды?", сверяем текст ответа с ОР')
    def test_rent_time_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_rent_time_question()
        main_page.click_to_rent_time_question_button()
        main_page.check_rent_time_answer_is_visible()
        actual_answer_text = main_page.get_rent_time_answer_text()
        expected_answer_text = ExpectedAnswers.RENT_TIME

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о возможности заказа на сегодня (вопрос №4)')
    @allure.description('Кликаем на вопрос "Можно ли заказать самокат прямо на сегодня?", сверяем текст ответа с ОР')
    def test_rent_for_today_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_rent_for_today_question()
        main_page.click_to_rent_for_today_question_button()
        main_page.check_rent_for_today_answer_is_visible()
        actual_answer_text = main_page.get_rent_for_today_answer_text()
        expected_answer_text = ExpectedAnswers.RENT_FOR_TODAY

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о возможности продления или раннего возврата самоката (вопрос №5)')
    @allure.description('Кликаем на вопрос "Можно ли продлить заказ или вернуть самокат раньше?", сверяем текст ответа с ОР')
    def test_rent_extension_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_rent_extension_question()
        main_page.click_to_rent_extension_question_button()
        main_page.check_rent_extension_answer_is_visible()
        actual_answer_text = main_page.get_rent_extension_answer_text()
        expected_answer_text = ExpectedAnswers.RENT_EXTENSION

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о наличии зарядки (вопрос №6)')
    @allure.description('Кликаем на вопрос "Вы привозите зарядку вместе с самокатом?", сверяем текст ответа с ОР')
    def test_charging_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_charging_question()
        main_page.click_to_charging_question_button()
        main_page.check_charging_answer_is_visible()
        actual_answer_text = main_page.get_charging_answer_text()
        expected_answer_text = ExpectedAnswers.CHARGING

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о возможности отмены заказа (вопрос №7)')
    @allure.description('Кликаем на вопрос "Можно ли отменить заказ?", сверяем текст ответа с ОР')
    def test_order_cancel_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_order_cancel_question()
        main_page.click_to_order_cancel_question_button()
        main_page.check_order_cancel_answer_is_visible()
        actual_answer_text = main_page.get_order_cancel_answer_text()
        expected_answer_text = ExpectedAnswers.ORDER_CANCEL

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"

    @allure.title('Тест на соответствие текста ответа на вопрос о возможности доставки за МКАД (вопрос №8)')
    @allure.description('Кликаем на вопрос "Я живу за МКАДом, привезёте?", сверяем текст ответа с ОР')
    def test_over_the_mkad_click_to_question_button_shows_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_over_the_mkad_question()
        main_page.click_to_over_the_mkad_question_button()
        main_page.check_over_the_mkad_answer_is_visible()
        actual_answer_text = main_page.get_over_the_mkad_answer_text()
        expected_answer_text = ExpectedAnswers.OVER_THE_MKAD

        assert actual_answer_text == expected_answer_text, "Текст не соответствует ОР"
