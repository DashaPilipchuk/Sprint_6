import pytest
import allure

from locators.order_scooter_page_locators import OrderScooterPageLocators
from locators.scooter_page_locators import ScooterPageLocators
from pages.order_scooter_page import OrderScooterPage


class TestOrderScooterPage:
    @allure.step('Оформление заказа')
    @allure.description('Проверка успещной авторизации')
    @pytest.mark.parametrize("name, surname, telephone_number", [('Иван', "Иванов", "89999999999"), ('Мария', "Павлова", "89998888888")])
    def test_popup_success_message(self, driver, name, surname, telephone_number):
        order_scooter_page = OrderScooterPage(driver)
        order_scooter_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/order')
        order_scooter_page.fill_name_field(name)
        order_scooter_page.fill_surname_field(surname)
        order_scooter_page.fill_metro_station_field()
        order_scooter_page.fill_telephone_number_field(telephone_number)
        order_scooter_page.click_on_next_button()
        order_scooter_page.fill_date_field()
        order_scooter_page.fill_scooter_period_field()
        order_scooter_page.fill_scooter_colour_field()
        order_scooter_page.click_on_order_button()
        order_scooter_page.click_on_submit_button()
        assert order_scooter_page.find_element_located(OrderScooterPageLocators.SUCCESS_MESSAGE)

    @allure.step('Переходим на стартовую страницу Яндекс Самоката из формы оформления заказа')
    def test_go_to_scooter_page_from_order_page(self, driver):
        order_scooter_page = OrderScooterPage(driver)
        order_scooter_page.go_to_site_scooter('https://qa-scooter.praktikum-services.ru/order')
        order_scooter_page.click_on_scooter_logo()
        assert order_scooter_page.find_element_located(ScooterPageLocators.HOME_LOGO)