from selenium import webdriver
from locators import *


class Test_Constructor:
    def test_constructor_go_to_sauces(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*constructor.BUTTON_SAUCE).click()
        element = driver.find_element(*constructor.TEXT_SAUCE)

        assert element.text =='Соусы'



    def test_constructor_go_to_bun(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*constructor.BUTTON_SAUCE).click()
        driver.find_element(*constructor.BUTTON_BUN).click()
        element = driver.find_element(*constructor.TEXT_BUN)

        assert element.text == 'Булки'




    def test_constructor_go_to_filling(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*constructor.BUTTON_SAUCE).click()
        driver.find_element(*constructor.BUTTON_FILLING).click()
        element = driver.find_element(*constructor.TEXT_FILLING)

        assert element.text == 'Начинки'

