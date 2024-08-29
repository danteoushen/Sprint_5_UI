import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


class Test_Login_to_account:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_button_login_to_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*Log_In_Account.LOG_IN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Registration.EMAIL)))

        driver.find_element(*Registration.NAME).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Log_In_Account.LOG_IN).click()

    # вход по кнопке «Личный кабинет» на главной
    def test_login_button_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*Log_In_Account.LOG_IN_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Registration.EMAIL)))

        driver.find_element(*Registration.EMAIL).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Log_In_Account.LOG_IN).click()

    # вход по кнопке на форме регистрации
    def test_login_button_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*Log_In_Account.LOG_IN_REGISTRATION_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Registration.EMAIL)))

        driver.find_element(*Registration.EMAIL).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Log_In_Account.LOG_IN).click()

    # вход через кнопку в форме восстановления пароля
    def test_login_button_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(*Log_In_Account.LOG_IN_REGISTRATION_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Registration.EMAIL)))

        driver.find_element(*Registration.EMAIL).send_keys('Alena_Dorofeeva_13_123@mail.ru')
        driver.find_element(*Registration.PASSWORD).send_keys('123456')
        driver.find_element(*Log_In_Account.LOG_IN).click()
