from locators.order_scooter_page_locators import OrderScooterPageLocators
from locators.scooter_page_locators import ScooterPageLocators
from pages.scooter_page import ScooterPage
from const import Constants
import allure


class TestScooterPage:
    @allure.title('Переходим к форме оформления заказ по кнопке "Заказать" в правом верхнем углу')
    def test_go_to_order_scooter_page_from_order_button(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page.click_on_order_button()
        assert scooter_page.find_element_located(OrderScooterPageLocators.ORDER_FORM)

    @allure.title('Переходим к форме оформления заказ по кнопке "Заказать" после скролла страницы')
    def test_go_to_order_scooter_page_from_order_button_after_scroll(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page.scrolling_to_order_button()
        scooter_page.find_element_located_click(ScooterPageLocators.ORDER_BUTTON_AFTER_SCROLLING)
        assert scooter_page.find_element_located(OrderScooterPageLocators.ORDER_FORM)

    @allure.title('Переходим на страницу dzen.ru по клику на лого Яндекс')
    def test_go_to_dzen_page_from_scooter_page(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/')
        scooter_page.go_to_dzen_page_from_scooter_page()
        assert scooter_page.go_to_new_window(Constants.SITE_NAME)
