import allure
from selenium.webdriver.common.by import By
from ..locators.main_page_locators import MainPageLocators
from ..pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Скролл до вопроса')
    def scroll_to_question(self, question_id):
        self.scroll_to_element([By.ID, "accordion__heading-" + str(question_id)])

    @allure.step('Клик по вопросу')
    def click_to_question_button(self, question_id):
        self.click_to_element([By.ID, "accordion__heading-" + str(question_id)])

    @allure.step('Проверяем видимость ответа на вопрос')
    def check_answer_is_visible(self, question_id):
        self.wait_for_visibility_of_element([By.ID, "accordion__panel-" + str(question_id)])

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, question_id):
        return self.get_text_of_the_element([By.ID, "accordion__panel-" + str(question_id)])

    @allure.step('Скролл до кнопки "Заказать" внизу страницы')
    def scroll_to_make_order_button(self):
        self.scroll_to_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать" внизу страницы')
    def click_to_make_order_button(self):
        self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON)