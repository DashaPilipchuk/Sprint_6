from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    QUESTIONS_PAGE = (By.XPATH, "//div[text()='Вопросы о важном']")
    HOW_MUCH_BUTTON = (By.ID, 'accordion__heading-0')
    HOW_MUCH_TEXT = (By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    SEVERAL_SCOOTER_BUTTON = (By.ID, 'accordion__heading-1')
    SEVERAL_SCOOTER_TEXT = (By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите "
                                      "покататься с друзьями, можете просто сделать несколько заказов — один за "
                                      "другим.']")
    RENTAL_TIME_BUTTON = (By.ID, 'accordion__heading-2')
    RENTAL_TIME_TEXT = (By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в "
                                  "течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ "
                                  "курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая "
                                  "в 20:30.']")
    TODAY_ORDER_BUTTON = (By.ID, 'accordion__heading-3')
    TODAY_ORDER_TEXT = (By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    SCOOTER_TIME_BUTTON = (By.ID, 'accordion__heading-4')
    SCOOTER_TIME_TEXT = (By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в "
                                   "поддержку по красивому номеру 1010.']")
    SCOOTER_CHARGE_BUTTON = (By.ID, 'accordion__heading-5')
    SCOOTER_CHARGE_TEXT = (By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
                                     "суток — даже если будете кататься без передышек и во сне. Зарядка не "
                                     "понадобится.']")
    CANCEL_ORDER_BUTTON = (By.ID, 'accordion__heading-6')
    CANCEL_ORDER_TEXT = (By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки "
                                   "тоже не попросим. Все же свои.']")
    PLACE_ORDER_BUTTON = (By.ID, 'accordion__heading-7')
    PLACE_ORDER_TEXT = (By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")



