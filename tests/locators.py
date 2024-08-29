from selenium.webdriver.common.by import By

class Registration:
#Имя
    NAME = (By.XPATH, "//input[@name='name']")
#EMAIL
    EMAIL = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
#Пароль
    PASSWORD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
#Кнопка Зарегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
#Сообщение об ошибке
    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")

class Log_In_Account:
#Кнопка Войти в аккаунт
    LOG_IN_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")
#Кнопка Личный Кабинет
    LOG_IN_PROFILE = (By.XPATH, ".//p[text()='Личный Кабинет']")
#Кнопка Войти
    LOG_IN = (By.XPATH, ".//button[text()='Войти']")
#Кнопка Войти на форме регистрации
    LOG_IN_REGISTRATION_FORM = (By.CLASS_NAME, "Auth_link__1fOlj")

class MainPage:
# Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
#кнопка логотипа
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
#Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class constructor:
#Раздел соусы
    BUTTON_SAUCE = (By.XPATH, ".//span[text()='Соусы']")
#Текст соусы
    TEXT_SAUCE = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
#Раздел булки
    BUTTON_BUN = (By.XPATH, ".//span[text()='Булки']")
#Текст булки
    TEXT_BUN = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
#Раздел начинки
    BUTTON_FILLING = (By.XPATH, ".//span[text()='Начинки']")
#Текст начинки
    TEXT_FILLING = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
