from locators.questions_page_locators import QuestionsPageLocators
from locators.scooter_page_locators import ScooterPageLocators
from pages.base_page import BasePage


class ScooterPage(BasePage):
    def scrolling_to_questions_page(self):
        questions_page = self.find_element_located(QuestionsPageLocators.QUESTIONS_PAGE)
        return self.driver.execute_script("arguments[0].scrollIntoView();", questions_page)

    def click_on_order_button(self):
        return self.find_element_located_click(ScooterPageLocators.ORDER_BUTTON)

    def scrolling_to_order_button(self):
        order_button = self.find_element_located(ScooterPageLocators.ORDER_BUTTON_AFTER_SCROLLING)
        return self.driver.execute_script("arguments[0].scrollIntoView();", order_button)

    def go_to_dzen_page_from_scooter_page(self):
        return self.find_element_located_click(ScooterPageLocators.YA_LOGO)