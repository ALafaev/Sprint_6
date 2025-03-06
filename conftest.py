from selenium import webdriver
from urls import URL
import pytest

@pytest.fixture(scope="function") # Запуск браузера
def driver():
    driver = webdriver.Firefox()
    driver.get(URL.HOME_PAGE_URL)
    yield driver
    driver.quit()