import time
import allure
from pages.textbox_page import TextBoxPage
from pages.form_page import FormPage
from pages.checkbox_page import CheckBoxPage
from pages.radio_button_page import RadioButtonPage


@allure.suite("Elements")
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
            assert f"{person.first_name} {person.last_name}" == result[0], "Поля имя и фамилия не заполнено"
            assert person.email == result[1], "форма email не заполнено"

    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, "Fullname does not match!"
            assert email == output_email, "Email does not match!"
            assert current_address == output_cur_address, "Current address does not match!"
            assert permanent_address == output_per_address, "Permanent address does not match!"

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title('Check Checkbox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            page.open()
            page.click_rb('yes')
            output_yes = page.get_output_result()
            page.click_rb('impressive')
            output_impressive = page.get_output_result()
            page.click_rb('no')
            output_no = page.get_output_result()
            assert output_yes == "Yes", "'YES' have not been selected"
            assert output_impressive == "Impressive", "'IMPRESSIVE' have not been selected"
            assert output_no == "No", "'NO' have not been selected"




































