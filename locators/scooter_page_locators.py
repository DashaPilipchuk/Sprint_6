from selenium.webdriver.common.by import By


class ScooterPageLocators:
    ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_AFTER_SCROLLING = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    HOME_LOGO = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
    YA_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")
