from locators.order_scooter_page_locators import OrderScooterPageLocators
from pages.base_page import BasePage
import allure


class OrderScooterPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def fill_name_field(self, name):
        return self.find_element_located_send_keys(OrderScooterPageLocators.NAME_FIELD, name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_surname_field(self, surname):
        return self.find_element_located_send_keys(OrderScooterPageLocators.SURNAME_FIELD, surname)

    @allure.step('Заполнить поле "Станция метро"')
    def fill_metro_station_field(self):
        self.find_element_located_click(OrderScooterPageLocators.METRO_STATION_FIELD)
        return self.find_element_located_click(OrderScooterPageLocators.METRO_STATION_BUTTON)

    @allure.step('Заполнить поле "Номер телефона"')
    def fill_telephone_number_field(self, telephone_number):
        return self.find_element_located_send_keys(OrderScooterPageLocators.TELEPHONE_NUMBER_FIELD, telephone_number)

    @allure.step('Клик на кнопку "Далее"')
    def click_on_next_button(self):
        return self.find_element_located_click(OrderScooterPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить поле "Дата"')
    def fill_date_field(self):
        self.find_element_located_click(OrderScooterPageLocators.DATE_FIELD)
        return self.find_element_located_click(OrderScooterPageLocators.CALENDAR_BUTTON)

    @allure.step('Заполнить поле "Срок аренды"')
    def fill_scooter_period_field(self):
        self.find_element_located_click(OrderScooterPageLocators.RENTAL_PERIOD_FIELD)
        return self.find_element_located_click(OrderScooterPageLocators.DAY_PERIOD_BUTTON)

    @allure.step('Заполнить поле "Цвет самоката')
    def fill_scooter_colour_field(self):
        return self.find_element_located_click(OrderScooterPageLocators.SCOOTER_COLOUR_BUTTON)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button(self):
        return self.find_element_located_click(OrderScooterPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждение заказа, клик по кнопке "Да"')
    def click_on_submit_button(self):
        return self.find_element_located_click(OrderScooterPageLocators.SUBMIT_BUTTON)

    @allure.step('Клик по слову "Самокат"')
    def click_on_scooter_logo(self):
        return self.find_element_located_click(OrderScooterPageLocators.SCOOTER_LOGO)
