from locators.questions_page_locators import QuestionsPageLocators
from pages.questions_page import QuestionsPage
from pages.scooter_page import ScooterPage
import allure
import pytest
from const import Constants


class TestQuestionsPage:
    @allure.title('Tecт на проверку соответствия текста в ответе на популярный вопрос')
    @pytest.mark.parametrize('locator, answer, answer_text', [
        (QuestionsPageLocators.HOW_MUCH_BUTTON, QuestionsPageLocators.HOW_MUCH_ANSWER, Constants.HOW_MUCH_TEXT),
        (QuestionsPageLocators.SEVERAL_SCOOTER_BUTTON, QuestionsPageLocators.SEVERAL_SCOOTER_ANSWER,
         Constants.SEVERAL_SCOOTER_TEXT),
        (QuestionsPageLocators.RENTAL_TIME_BUTTON, QuestionsPageLocators.RENTAL_TIME_ANSWER, Constants.RENTAL_TIME_TEXT),
        (QuestionsPageLocators.TODAY_ORDER_BUTTON, QuestionsPageLocators.TODAY_ORDER_ANSWER, Constants.TODAY_ORDER_TEXT),
        (QuestionsPageLocators.SCOOTER_TIME_BUTTON, QuestionsPageLocators.SCOOTER_TIME_ANSWER,
         Constants.SCOOTER_TIME_TEXT),
        (QuestionsPageLocators.SCOOTER_CHARGE_BUTTON, QuestionsPageLocators.SCOOTER_CHARGE_ANSWER,
         Constants.SCOOTER_CHARGE_TEXT),
        (QuestionsPageLocators.CANCEL_ORDER_BUTTON, QuestionsPageLocators.CANCEL_ORDER_ANSWER,
         Constants.CANCEL_ORDER_TEXT),
        (QuestionsPageLocators.PLACE_ORDER_BUTTON, QuestionsPageLocators.PLACE_ORDER_ANSWER, Constants.PLACE_ORDER_TEXT)])
    def test_click_on_drop_down_how_much_question(self, driver, locator, answer, answer_text):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page = ScooterPage(driver)
        scooter_page.scrolling_to_questions_page()
        questions_page.click_on_drop_down(locator)
        assert answer_text in questions_page.get_text_of_element(answer)



