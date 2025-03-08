import allure
from selenium.webdriver.common.by import By
from ..pages.base_page import BasePage
import random, datetime

class AboutRentLocators:
    DATE_INPUT = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']  # Поле ввода даты
    RENTAL_PERIOD_INPUT = [By.CLASS_NAME, 'Dropdown-arrow']  # Поле выбора срока аренды
    RENTAL_PERIOD_ONE_DAY = [By.XPATH, './/div[@class="Dropdown-option" and text()="сутки"]'] # период аренды "сутки"
    RENTAL_PERIOD_TWO_DAYS = [By.XPATH, './/div[@class="Dropdown-option" and text()="двое суток"]'] # период аренды "двое суток"
    SCOOTER_COLOR_CHECKBOX_BLACK = [By.XPATH, './/input[@id="black"]'] # Чекбокс выбора цвета "Черный жемчуг"
    SCOOTER_COLOR_CHECKBOX_GREY = [By.XPATH, './/input[@id="grey"]'] # Чекбокс выбора цвета "Серая безысходность"
    COMMENT_INPUT = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]'] # Поле ввода комментария
    MAKE_ORDER_BUTTON = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]//button[text()="Заказать"]'] # Кнопка "Заказать"
    CONFIRM_ORDER_BUTTON = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]//button[text()="Да"]']  # Кнопка "Да"
    SHOW_STATUS_BUTTON = [By.XPATH, './/button[text()="Посмотреть статус"]'] # Кнопка "Посмотреть статус"


class AboutRentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Рандомный выбор даты для поля "Когда привезти самокат"')
    def choose_date(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        date = random.choice((today, tomorrow))
        return date.strftime('%d.%m.%Y')

    @allure.step('Заполняем поле "Когда привезти самокат"')
    def filling_the_date_field(self):
        self.filling_the_field(AboutRentLocators.DATE_INPUT, self.choose_date())

    @allure.step('Клик по полю "Срок аренды"')
    def click_to_rental_period_field(self):
        self.click_to_element(AboutRentLocators.RENTAL_PERIOD_INPUT)

    @allure.step('Клик по нужному периоду аренды из выпадающего списка')
    def click_to_rental_period_variant(self, period_name):
        if period_name == 'сутки':
            self.click_to_element(AboutRentLocators.RENTAL_PERIOD_ONE_DAY)
        else:
            self.click_to_element(AboutRentLocators.RENTAL_PERIOD_TWO_DAYS)

    @allure.step('Заполняем поле "Срок аренды"')
    def filling_the_rental_period_field(self, period_name):
        self.click_to_rental_period_field()
        self.click_to_rental_period_variant(period_name)

    @allure.step('Клик по чекбоксу выбора цвета')
    def click_to_scooter_color_checkbox(self):
        locator = random.choice((AboutRentLocators.SCOOTER_COLOR_CHECKBOX_BLACK, AboutRentLocators.SCOOTER_COLOR_CHECKBOX_GREY))
        self.click_to_element(locator)

    @allure.step('Заполняем поле "Комментарий"')
    def filling_the_comment_field(self, comment):
        self.filling_the_field(AboutRentLocators.COMMENT_INPUT, comment)

    @allure.step('Клик по кнопке "Заказать"')
    def click_to_make_order_button(self):
        self.click_to_element(AboutRentLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверяем, что кнопка "Да" кликабельна')
    def check_confirm_order_button_is_clickable(self):
        self.wait_for_element_to_be_clickable(AboutRentLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Да"')
    def click_to_confirm_order_button(self):
        self.click_to_element(AboutRentLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверяем, что кнопка "Посмотреть статус" активна')
    def check_show_status_button_is_enabled(self):
        return self.check_element_is_enabled(AboutRentLocators.SHOW_STATUS_BUTTON)