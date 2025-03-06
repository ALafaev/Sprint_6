from selenium.webdriver.common.by import By

class QuestionsLocators:
    PRICE_AND_PAYMENT_BUTTON = (By.ID, 'accordion__heading-0')  # Кнопка "Сколько это стоит? И как оплатить?"
    FEW_SCOOTERS_RENT_BUTTON = (By.ID, 'accordion__heading-1')  # Кнопка "Хочу сразу несколько самокатов! Так можно?"
    RENT_TIME_BUTTON = (By.ID, 'accordion__heading-2')  # Кнопка "Как рассчитывается время аренды?"
    RENT_FOR_TODAY_BUTTON = (By.ID, 'accordion__heading-3')  # Кнопка "Можно ли заказать самокат прямо на сегодня?"
    RENT_EXTENSION_BUTTON = (By.ID, 'accordion__heading-4')  # Кнопка "Можно ли продлить заказ или вернуть самокат раньше?"
    CHARGING_BUTTON = (By.ID, 'accordion__heading-5')  # Кнопка "Вы привозите зарядку вместе с самокатом?"
    ORDER_CANCEL_BUTTON = (By.ID, 'accordion__heading-6')  # Кнопка "Можно ли отменить заказ?"
    OVER_THE_MKAD_BUTTON = (By.ID, 'accordion__heading-7')  # Кнопка "Я живу за МКАДом, привезёте?"

class AnswersLocators:
    PRICE_AND_PAYMENT_ANSWER = [By.ID, 'accordion__panel-0'] # Ответ на вопрос "Сколько это стоит? И как оплатить?"
    FEW_SCOOTERS_RENT_ANSWER = [By.ID, 'accordion__panel-1'] # Ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"
    RENT_TIME_ANSWER = [By.ID, 'accordion__panel-2'] # Ответ на вопрос "Как рассчитывается время аренды?"
    RENT_FOR_TODAY_ANSWER = [By.ID, 'accordion__panel-3'] # Ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"
    RENT_EXTENSION_ANSWER = [By.ID, 'accordion__panel-4'] # Ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    CHARGING_ANSWER = [By.ID, 'accordion__panel-5'] # Ответ на вопрос "Вы привозите зарядку вместе с самокатом?"
    ORDER_CANCEL_ANSWER = [By.ID, 'accordion__panel-6'] # Ответ на вопрос "Можно ли отменить заказ?"
    OVER_THE_MKAD_ANSWER = [By.ID, 'accordion__panel-7'] # Ответ на вопрос "Я живу за МКАДом, привезёте?"

class MainPageLocators:
    MAKE_ORDER_BUTTON = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']




