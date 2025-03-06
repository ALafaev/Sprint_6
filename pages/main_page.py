import allure
from ..locators.main_page_locators import QuestionsLocators, AnswersLocators, MainPageLocators
from ..pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Методы для прокрутки страницы до нужного вопроса:

    @allure.step('Скролл до вопроса "Сколько это стоит? И как оплатить?"')
    def scroll_to_prise_and_payment_question(self):
        self.scroll_to_element(QuestionsLocators.PRICE_AND_PAYMENT_BUTTON)

    @allure.step('Скролл до вопроса "Хочу сразу несколько самокатов! Так можно?"')
    def scroll_to_few_scooters_rent_question(self):
        self.scroll_to_element(QuestionsLocators.FEW_SCOOTERS_RENT_BUTTON)

    @allure.step('Скролл до вопроса "Как рассчитывается время аренды?"')
    def scroll_to_rent_time_question(self):
        self.scroll_to_element(QuestionsLocators.RENT_TIME_BUTTON)

    @allure.step('Скролл до вопроса "Можно ли заказать самокат прямо на сегодня?"')
    def scroll_to_rent_for_today_question(self):
        self.scroll_to_element(QuestionsLocators.RENT_FOR_TODAY_BUTTON)

    @allure.step('Скролл до вопроса "Можно ли продлить заказ или вернуть самокат раньше?"')
    def scroll_to_rent_extension_question(self):
        self.scroll_to_element(QuestionsLocators.RENT_EXTENSION_BUTTON)

    @allure.step('Скролл до вопроса "Вы привозите зарядку вместе с самокатом?"')
    def scroll_to_charging_question(self):
        self.scroll_to_element(QuestionsLocators.CHARGING_BUTTON)

    @allure.step('Скролл до вопроса "Можно ли отменить заказ?"')
    def scroll_to_order_cancel_question(self):
        self.scroll_to_element(QuestionsLocators.ORDER_CANCEL_BUTTON)

    @allure.step('Скролл до вопроса "Я живу за МКАДом, привезёте?"')
    def scroll_to_over_the_mkad_question(self):
        self.scroll_to_element(QuestionsLocators.OVER_THE_MKAD_BUTTON)

    # Методы для кликов по вопросам:

    @allure.step('Клик на вопрос "Сколько это стоит? И как оплатить?"')
    def click_to_price_and_payment_question_button(self):
        self.click_to_element(QuestionsLocators.PRICE_AND_PAYMENT_BUTTON)

    @allure.step('Клик на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def click_to_few_scooters_rent_question_button(self):
        self.click_to_element(QuestionsLocators.FEW_SCOOTERS_RENT_BUTTON)

    @allure.step('Клик на вопрос "Как рассчитывается время аренды?"')
    def click_to_rent_time_question_button(self):
        self.click_to_element(QuestionsLocators.RENT_TIME_BUTTON)

    @allure.step('Клик на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def click_to_rent_for_today_question_button(self):
        self.click_to_element(QuestionsLocators.RENT_FOR_TODAY_BUTTON)

    @allure.step('Клик на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_to_rent_extension_question_button(self):
        self.click_to_element(QuestionsLocators.RENT_EXTENSION_BUTTON)

    @allure.step('Клик на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def click_to_charging_question_button(self):
        self.click_to_element(QuestionsLocators.CHARGING_BUTTON)

    @allure.step('Клик на вопрос "Можно ли отменить заказ?"')
    def click_to_order_cancel_question_button(self):
        self.click_to_element(QuestionsLocators.ORDER_CANCEL_BUTTON)

    @allure.step('Клик на вопрос "Я живу за МКАДом, привезёте?"')
    def click_to_over_the_mkad_question_button(self):
        self.click_to_element(QuestionsLocators.OVER_THE_MKAD_BUTTON)

    # Методы для получения фактического текста ответа на вопрос:

    @allure.step('Получаем текст ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def get_price_and_payment_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.PRICE_AND_PAYMENT_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def get_few_scooters_rent_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.FEW_SCOOTERS_RENT_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Как рассчитывается время аренды?"')
    def get_rent_time_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.RENT_TIME_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def get_rent_for_today_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.RENT_FOR_TODAY_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def get_rent_extension_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.RENT_EXTENSION_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def get_charging_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.CHARGING_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Можно ли отменить заказ?"')
    def get_order_cancel_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.ORDER_CANCEL_ANSWER)

    @allure.step('Получаем текст ответа на вопрос "Я живу за МКАДом, привезёте?"')
    def get_over_the_mkad_answer_text(self):
        return self.get_text_of_the_element(AnswersLocators.OVER_THE_MKAD_ANSWER)

    # Методы для ожидания видимости ответа на вопрос:

    @allure.step('Проверяем видимость ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def check_price_and_payment_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.PRICE_AND_PAYMENT_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def check_few_scooters_rent_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.FEW_SCOOTERS_RENT_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Как рассчитывается время аренды?"')
    def check_rent_time_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.RENT_TIME_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def check_rent_for_today_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.RENT_FOR_TODAY_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def check_rent_extension_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.RENT_EXTENSION_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def check_charging_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.CHARGING_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Можно ли отменить заказ?"')
    def check_order_cancel_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.ORDER_CANCEL_ANSWER)

    @allure.step('Проверяем видимость ответа на вопрос "Я живу за МКАДом, привезёте?"')
    def check_over_the_mkad_answer_is_visible(self):
        self.wait_for_visibility_of_element(AnswersLocators.OVER_THE_MKAD_ANSWER)

    @allure.step('Скролл до кнопки "Заказать" внизу страницы')
    def scroll_to_make_order_button(self):
        self.scroll_to_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать" внизу страницы')
    def click_to_make_order_button(self):
        self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON)