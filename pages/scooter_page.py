from locators.questions_page_locators import QuestionsPageLocators
from locators.scooter_page_locators import ScooterPageLocators
from pages.base_page import BasePage
import allure


class ScooterPage(BasePage):
    @allure.step('Скролл до страницы с популярными вопросами')
    def scrolling_to_questions_page(self):
        questions_page = self.find_element_located(QuestionsPageLocators.QUESTIONS_PAGE)
        return self.scrolling_page_to_element(questions_page)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button(self):
        return self.find_element_located_click(ScooterPageLocators.ORDER_BUTTON)

    @allure.step('Скролл до кнопки "Заказать"')
    def scrolling_to_order_button(self):
        order_button = self.find_element_located(ScooterPageLocators.ORDER_BUTTON_AFTER_SCROLLING)
        return self.scrolling_page_to_element(order_button)

    @allure.step('Редирект на страницу дзена по нажатию на лого')
    def go_to_dzen_page_from_scooter_page(self):
        return self.find_element_located_click(ScooterPageLocators.YA_LOGO)