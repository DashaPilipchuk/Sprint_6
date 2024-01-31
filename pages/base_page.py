from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы в браузере')
    def go_to_site_scooter(self, url):
        return self.driver.get(url)

    @allure.step('Найти элемент на странице по локатору')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f'Element not found in {locator}')

    @allure.step('Клик по элементу')
    def find_element_located_click(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator),
                                                      message=f'Element not found in {locator}').click()

    @allure.step('Заполнить поле')
    def find_element_located_send_keys(self, locator, field_name=str, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').send_keys(field_name)

    @allure.step('Скролл до элемента на странице')
    def scrolling_page_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, element):
        return self.find_element_located(element).text

    @allure.step('Перейти в новое окно')
    def go_to_new_window(self, site_name):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(site_name))


