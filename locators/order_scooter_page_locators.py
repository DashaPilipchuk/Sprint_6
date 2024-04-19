from selenium.webdriver.common.by import By


class OrderScooterPageLocators:
    ORDER_FORM = (By.XPATH, "//div[@class='Order_Form__17u6u']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@class='select-search__input']")
    METRO_STATION_BUTTON = (By.XPATH, "//button[@class='Order_SelectOption__82bhS select-search__option']/div[text("
                                      ")='Черкизовская']")
    TELEPHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_BUTTON =(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--001 "
                                "react-datepicker__day--outside-month']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-control')
    DAY_PERIOD_BUTTON = (By.XPATH, "//div[text()='сутки']")
    SCOOTER_COLOUR_BUTTON = (By.ID, 'black')
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Заказ оформлен']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

