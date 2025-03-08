import allure
from selenium.webdriver.common.by import By
from ..pages.base_page import BasePage

class HeaderLocators:
    MAKE_ORDER_BUTTON = [By.XPATH, './/button[text()="Заказать"]'] # Кнопка "Заказать"
    LOGO_YANDEX = [By.XPATH, './/img[@alt="Yandex"]'] # Логотип "Яндекс"
    LOGO_SCOOTER = [By.XPATH, './/img[@alt="Scooter"]'] # Логотип "Самокат"

class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Заказать" в хедере страницы')
    def click_to_make_order_button(self):
        self.click_to_element(HeaderLocators.MAKE_ORDER_BUTTON)

    @allure.step('Клик по логотипу "Самокат" в хедере страницы')
    def click_to_logo_scooter(self):
        self.click_to_element(HeaderLocators.LOGO_SCOOTER)

    @allure.step('Клик по логотипу "Яндекс" в хедере страницы')
    def click_to_logo_yandex(self):
        self.click_to_element(HeaderLocators.LOGO_YANDEX)

    @allure.step('Проверяем, что урл содержит "https://dzen.ru"')
    def check_url_contains_dzen(self):
        self.check_url_contains_value("https://dzen.ru")