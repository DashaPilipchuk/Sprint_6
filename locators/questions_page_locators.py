from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    QUESTIONS_PAGE = (By.XPATH, "//div[text()='Вопросы о важном']")
    HOW_MUCH_BUTTON = (By.ID, 'accordion__heading-0')
    HOW_MUCH_ANSWER = (By.ID, 'accordion__panel-0')
    SEVERAL_SCOOTER_BUTTON = (By.ID, 'accordion__heading-1')
    SEVERAL_SCOOTER_ANSWER = (By.ID, 'accordion__panel-1')
    RENTAL_TIME_BUTTON = (By.ID, 'accordion__heading-2')
    RENTAL_TIME_ANSWER = (By.ID, 'accordion__panel-2')
    TODAY_ORDER_BUTTON = (By.ID, 'accordion__heading-3')
    TODAY_ORDER_ANSWER = (By.ID, 'accordion__panel-3')
    SCOOTER_TIME_BUTTON = (By.ID, 'accordion__heading-4')
    SCOOTER_TIME_ANSWER = (By.ID, 'accordion__panel-4')
    SCOOTER_CHARGE_BUTTON = (By.ID, 'accordion__heading-5')
    SCOOTER_CHARGE_ANSWER = (By.ID, 'accordion__panel-5')
    CANCEL_ORDER_BUTTON = (By.ID, 'accordion__heading-6')
    CANCEL_ORDER_ANSWER = (By.ID, 'accordion__panel-6')
    PLACE_ORDER_BUTTON = (By.ID, 'accordion__heading-7')
    PLACE_ORDER_ANSWER = (By.ID, 'accordion__panel-7')



