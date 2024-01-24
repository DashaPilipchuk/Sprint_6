from locators.order_scooter_page_locators import OrderScooterPageLocators
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    def fill_name_field(self, name):
        return self.find_element_located(OrderScooterPageLocators.NAME_FIELD).send_keys(name)

    def fill_surname_field(self, surname):
        return self.find_element_located(OrderScooterPageLocators.SURNAME_FIELD).send_keys(surname)

    def fill_metro_station_field(self):
        self.find_element_located_click(OrderScooterPageLocators.METRO_STATION_FIELD)
        return self.find_element_located_click(OrderScooterPageLocators.METRO_STATION_BUTTON)

    def fill_telephone_number_field(self, telephone_number):
        return self.find_element_located(OrderScooterPageLocators.TELEPHONE_NUMBER_FIELD).send_keys(telephone_number)

    def click_on_next_button(self):
        return self.find_element_located_click(OrderScooterPageLocators.NEXT_BUTTON)

    def fill_date_field(self):
        self.find_element_located_click(OrderScooterPageLocators.DATE_FIELD)
        return self.find_element_located_click(OrderScooterPageLocators.CALENDAR_BUTTON)

    def fill_scooter_period_field(self):
        self.find_element_located_click(OrderScooterPageLocators.RENTAL_PERIOD_FIELD)
        return self.find_element_located_click(OrderScooterPageLocators.DAY_PERIOD_BUTTON)

    def fill_scooter_colour_field(self):
        return self.find_element_located_click(OrderScooterPageLocators.SCOOTER_COLOUR_BUTTON)

    def click_on_order_button(self):
        return self.find_element_located_click(OrderScooterPageLocators.ORDER_BUTTON)

    def click_on_submit_button(self):
        return self.find_element_located_click(OrderScooterPageLocators.SUBMIT_BUTTON)

    def click_on_scooter_logo(self):
        return self.find_element_located_click(OrderScooterPageLocators.SCOOTER_LOGO)




