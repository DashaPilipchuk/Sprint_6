from pages.base_page import BasePage


class QuestionsPage(BasePage):
    def click_on_drop_down(self, locator):
        return self.find_element_located_click(locator)

