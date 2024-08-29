from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

class Test_Personal_Account:

    # Переход в личный кабинет
    def test_personal_account_button(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*Log_In_Account.LOG_IN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Registration.EMAIL)))

        driver.find_element(*Registration.NAME).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Log_In_Account.LOG_IN).click()



        #Переход из личного кабинета в конструктор
    def test_constructor_button(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*MainPage.CONSTRUCTOR_BUTTON).click()



    #Выход из аккаунта
    def test_logout(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*Registration.NAME).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Log_In_Account.LOG_IN).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Log_In_Account.LOG_IN_PROFILE)))

        driver.find_element(*Log_In_Account.LOG_IN_PROFILE).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((MainPage.LOGOUT_BUTTON)))

        driver.find_element(*MainPage.LOGOUT_BUTTON).click()

