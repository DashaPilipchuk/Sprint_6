from pages.base_page import BasePage
import allure


class QuestionsPage(BasePage):
    @allure.step('Клик на кнопку выпадающего списка')
    def click_on_drop_down(self, locator):
        return self.find_element_located_click(locator)

