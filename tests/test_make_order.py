import allure
import pytest
from ..pages.header_page import HeaderPage
from ..pages.about_rent_page import AboutRentPage
from ..pages.whose_scooter_page import WhoseScooterPage
from ..pages.main_page import MainPage
from urls import URL
import data

class TestMakeOrder:

    @allure.title('Проверка успешного оформления заказа через кнопку "Заказать" в хедере')
    @allure.description('Кликаем на вопрос "Сколько это стоит? И как оплатить?", сверяем текст ответа с ОР')
    @pytest.mark.parametrize('i',[0,1])
    def test_price_and_payment_click_to_question_button_shows_answer(self, driver, i):
        header_page = HeaderPage(driver)
        header_page.click_to_make_order_button()

        whose_scooter_page = WhoseScooterPage(driver)
        whose_scooter_page.filling_the_name_field(data.ORDER_VALUES[i]['name'])
        whose_scooter_page.filling_the_surname_field(data.ORDER_VALUES[i]['surname'])
        whose_scooter_page.filling_the_address_field(data.ORDER_VALUES[i]['address'])
        whose_scooter_page.filling_the_metro_station_field(data.ORDER_VALUES[i]['metro'])
        whose_scooter_page.filling_the_phone_field(data.ORDER_VALUES[i]['phone'])
        whose_scooter_page.click_to_next_page_button()

        about_rent_page = AboutRentPage(driver)
        about_rent_page.filling_the_date_field()
        about_rent_page.filling_the_rental_period_field(data.ORDER_VALUES[i]['rental_period'])
        about_rent_page.click_to_scooter_color_checkbox()
        about_rent_page.filling_the_comment_field(data.ORDER_VALUES[i]['comment'])
        about_rent_page.click_to_make_order_button()
        about_rent_page.check_confirm_order_button_is_clickable()
        about_rent_page.click_to_confirm_order_button()

        assert about_rent_page.check_show_status_button_is_enabled() == True, "Сообщение об успешном оформлении заказа отсутствует"

    @allure.title('Проверка, что клик на кнопку "Заказать" внизу главной страницы ведет на форму "Для кого самокат?"')
    @allure.description('Ищем кнопку "Заказать" внизу главной страницы, жмем на нее, проверяем, что открылась страница "Для кого самокат?"')
    def test_click_to_main_page_make_order_button_open_whose_scooter_page(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_make_order_button()
        main_page.click_to_make_order_button()

        whose_scooter_page = WhoseScooterPage(driver)
        current_url = whose_scooter_page.get_current_url()

        assert current_url == URL.MAKE_ORDER_PAGE_URL, 'Переход на страницу "Для кого самокат?" не произошел'
