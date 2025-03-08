import allure
from ..pages.header_page import HeaderPage
from urls import URL

class TestLogoYandexScooter:

    @allure.title('Нажатие на логотип «Самоката» ведет на главную страницу «Самоката»')
    @allure.description('Кликаем на логотип «Самоката» в хедере, сверяем урл с урлом главной страницы')
    def test_click_to_scooter_logo_open_home_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_to_make_order_button()
        header_page.click_to_logo_scooter()

        assert header_page.get_current_url() == URL.HOME_PAGE_URL, "Урл не совпадает с ожидаемым"

    @allure.title('Проверяем, что при нажатии на логотип «Яндекс» в новом окне через редирект откроется главная страница Дзена')
    @allure.description('Кликаем на логотип «Яндекс» в хедере, проверяем, что урл содержит ссылку на главную страницу Дзена')
    def test_click_to_yandex_logo_open_dzen_main_page_in_new_tab(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_to_logo_yandex()
        header_page.switch_to_new_window()
        header_page.check_url_contains_dzen()
        current_url = header_page.get_current_url()
        assert 'dzen.ru' in current_url, "Урл не совпадает с ожидаемым"
