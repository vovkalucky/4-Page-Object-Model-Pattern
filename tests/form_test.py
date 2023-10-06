import random
import time
import allure
import pytest
from pages.form_page import FormPage
@allure.suite("Form")
class TestElements:
    @allure.feature('FormPage')
    class TestFormPage:
        @allure.title('Check FormPage')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person = form_page.fill_fields_and_submit()
            result = form_page.form_result()

            print(f'Person: {person}')
            print((f'Result: {result}'))
            assert f"{person.first_name} {person.last_name}" == result[0], "Поля имя и фамилия не заполнены"
            assert person.email == result[1], "форма email не заполнена"
            #assert person.gender == result[2], "Пол не заполнен"
            assert person.mobile == result[3], "Мобильный номер не заполнен"
            #assert person.date_of_birth == result[4], "Мобильный номер не заполнен"
