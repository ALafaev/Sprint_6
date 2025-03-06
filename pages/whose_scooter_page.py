import allure
from selenium.webdriver.common.by import By
from ..pages.base_page import BasePage

class WhoseScooterLocators:
    NAME_INPUT = [By.XPATH, './/input[@placeholder="* Имя"]'] # Поле ввода имени
    SURNAME_INPUT = [By.XPATH, './/input[@placeholder="* Фамилия"]'] # Поле ввода фамилии
    ADDRESS_INPUT = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'] # Поле ввода адреса
    METRO_STATION_INPUT = [By.XPATH, './/input[@placeholder="* Станция метро"]'] # Поле выбора станции метро
    PHONE_INPUT = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'] # Поле ввода номера телефона
    METRO_STATION_SOKOLNIKI = [By.XPATH, './/*[text()="Сокольники"]'] # Станция "Сокольники" в выпадающем списке
    METRO_STATION_LUBYANKA = [By.XPATH, './/*[text()="Лубянка"]'] # Станция "Лубянка" в выпадающем списке
    NEXT_PAGE_BUTTON = [By.XPATH, './/button[text()="Далее"]'] # Кнопка "Далее"


class WhoseScooterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поле "Имя"')
    def filling_the_name_field(self, name):
        self.filling_the_field(WhoseScooterLocators.NAME_INPUT, name)

    @allure.step('Заполняем поле "Фамилия"')
    def filling_the_surname_field(self, surname):
        self.filling_the_field(WhoseScooterLocators.SURNAME_INPUT, surname)

    @allure.step('Заполняем поле "Адрес"')
    def filling_the_address_field(self, address):
        self.filling_the_field(WhoseScooterLocators.ADDRESS_INPUT, address)

    @allure.step('Заполняем поле "Номер телефона"')
    def filling_the_phone_field(self, phone):
        self.filling_the_field(WhoseScooterLocators.PHONE_INPUT, phone)

    @allure.step('Ввод значения в поле "Станция метро"')
    def enter_data_to_the_metro_station_field(self, station_name):
        self.filling_the_field(WhoseScooterLocators.METRO_STATION_INPUT, station_name)

    @allure.step('Клик по нужной станции метро в выпадающем списке')
    def click_to_metro_station_name(self, station_name):
        if station_name == 'Сокольники':
            self.click_to_element(WhoseScooterLocators.METRO_STATION_SOKOLNIKI)
        elif station_name == 'Лубянка':
            self.click_to_element(WhoseScooterLocators.METRO_STATION_LUBYANKA)
        else:
            print('Выбранная станция не найдена')

    @allure.step('Заполняем поле "Станция метро"')
    def filling_the_metro_station_field(self, station_name):
        self.enter_data_to_the_metro_station_field(station_name)
        self.click_to_metro_station_name(station_name)

    @allure.step('Клик по кнопке "Далее"')
    def click_to_next_page_button(self):
        self.click_to_element(WhoseScooterLocators.NEXT_PAGE_BUTTON)
