from locators.questions_page_locators import QuestionsPageLocators
from pages.questions_page import QuestionsPage
from pages.scooter_page import ScooterPage
import allure


class TestQuestionsPage:
    @allure.step('Кликаем на вопрос "Сколько это стоит? И как оплатить?"')
    def test_click_on_drop_down_how_much_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.HOW_MUCH_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.HOW_MUCH_TEXT)

    @allure.step('Кликаем на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def test_click_on_drop_down_several_scooters_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.SEVERAL_SCOOTER_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.SEVERAL_SCOOTER_TEXT)

    @allure.step('Кликаем на вопрос "Как рассчитывается время аренды?"')
    def test_click_on_drop_down_rental_time_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.RENTAL_TIME_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.RENTAL_TIME_TEXT)

    @allure.step('Кликаем на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_click_on_drop_down_today_order_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.TODAY_ORDER_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.TODAY_ORDER_TEXT)

    @allure.step('Кликаем на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_click_on_drop_down_scooter_time(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.SCOOTER_TIME_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.SCOOTER_TIME_TEXT)

    @allure.step('Кликаем на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_click_on_drop_down_scooter_charge(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.SCOOTER_CHARGE_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.SCOOTER_CHARGE_TEXT)

    @allure.step('Кликаем на вопрос "Можно ли отменить заказ?"')
    def test_click_on_drop_down_cancel_order(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.CANCEL_ORDER_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.CANCEL_ORDER_TEXT)

    @allure.step('Кликаем на вопрос "Я жизу за МКАДом, привезёте?"')
    def test_click_on_drop_down_place_order(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(QuestionsPageLocators.PLACE_ORDER_BUTTON)
        assert questions_page.find_element_located(QuestionsPageLocators.PLACE_ORDER_TEXT)

