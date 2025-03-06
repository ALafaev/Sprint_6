from selenium.webdriver.common.by import By

class BasePageLocators:
    QUESTIONS_TITLE = (By.XPATH, './/div[text()="Вопросы о важном"]')  # Заголовок "Вопросы о важном"
    COOKIE_POPUP_BUTTON = [By.ID, 'rcc-confirm-button'] # кнопка "да все привыкли" на попапе об использвании cookie