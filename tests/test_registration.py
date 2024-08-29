import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

class Test_Registration:

    #Регистрация с корректными данными
    def test_registration_correct(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")


        driver.find_element(*Registration.NAME).send_keys('Алена')
        driver.find_element(*Registration.EMAIL).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Registration.REGISTRATION_BUTTON).click()


    # Регистрация с некорректными паролем
    def test_registration_incorrect_password(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*Registration.NAME).send_keys('Алена')
        driver.find_element(*Registration.EMAIL).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123')
        driver.find_element(*Registration.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.ERROR_MESSAGE)))
        error_message = driver.find_element(*Registration.ERROR_MESSAGE).text
        assert error_message == 'Некорректный пароль'

