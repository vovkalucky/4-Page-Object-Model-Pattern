import time
import allure
import pytest
from pages.textbox_page import TextBoxPage
from pages.checkbox_page import CheckBoxPage
from pages.radio_button_page import RadioButtonPage
from pages.webtable_page import WebtablePage
from pages.button_page import ButtonPage
from pages.link_page import LinkPage
from pages.upload_and_download_page import UploadAndDownloadPage
from pages.dynamic_elements_page import DynamicElementsPage


@allure.suite("Elements")
class TestElements:

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
        @pytest.mark.xfail
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

    @allure.feature('Webtable')
    class TestWebtablePage:
        @allure.title('Add person')
        def test_webtable_add_person(self, driver):
            page = WebtablePage(driver, 'https://demoqa.com/webtables')
            page.open()
            new_person = page.add_person()
            time.sleep(2)
            table_result = page.check_new_added_person()
            assert new_person in table_result, "Person does not added in the table"

        @allure.title('Search person')
        def test_webtable_search_person(self, driver):
            page = WebtablePage(driver, 'https://demoqa.com/webtables')
            page.open()
            keyword = page.add_person()[3] #[random.randint(0, 5)]
            time.sleep(3)
            page.search_person(keyword)
            time.sleep(3)
            row = page.check_search_person()
            assert keyword in row, "Search does not work correctly!"

        @allure.title('Edit person')
        def test_webtable_edit_person(self, driver):
            page = WebtablePage(driver, 'https://demoqa.com/webtables')
            page.open()
            person = page.add_person()
            name = person[1]
            page.search_person(name)
            result_expected = page.update_person_info()
            row = page.check_search_person()
            print(result_expected)
            print(row)
            assert result_expected in row, "Edit not good!"

        @allure.title('Delete person')
        def test_delete_person(self, driver):
            page = WebtablePage(driver, 'https://demoqa.com/webtables')
            page.open()
            email = page.add_person()[3]
            time.sleep(1)
            page.search_person(email)
            time.sleep(2)
            page.delete_person()
            result_actual = page.check_delete()
            result_expected = "No rows found"
            assert result_actual == result_expected, "Delete person does not work"

        @allure.title('Change count rows')
        def test_change_count_rows(self, driver):
            page = WebtablePage(driver, 'https://demoqa.com/webtables')
            page.open()
            page.remove_footer()
            page.remove_fixedban()
            result_fact = page.select_change_rows()
            result_expected = [5, 10, 20, 25, 50, 100]
            assert result_fact == result_expected, "The number in rows does not change correctly"

    @allure.feature('ButtonPage')
    class TestButtonPage:
        @allure.title('Button double click')
        def test_double_click_on_button(self, driver):
            page = ButtonPage(driver, 'https://demoqa.com/buttons')
            page.open()
            page.double_click_on_button(driver)
            result_fact = page.check_double_click_on_button()
            result_expected = "You have done a double click"
            assert result_fact == result_expected, "Double click does not work correctly!"

        @allure.title('Dynamic Button click')
        def test_click_on_button(self, driver):
            page = ButtonPage(driver, 'https://demoqa.com/buttons')
            page.open()
            page.click_on_button()
            result_fact = page.check_click_on_button()
            result_expected = "You have done a dynamic click"
            assert result_fact == result_expected, "Click does not work correctly!"

        @allure.title('Button right click')
        def test_right_click_on_button(self, driver):
            page = ButtonPage(driver, 'https://demoqa.com/buttons')
            page.open()
            page.right_click_on_button(driver)
            result_fact = page.check_right_click_on_button()
            result_expected = "You have done a right click"
            assert result_fact == result_expected, "Right click does not work correctly!"

    @allure.feature('Links')
    class TestLinkPage:
        @allure.title('Check link')
        def test_check_link(self, driver):
            page = LinkPage(driver, 'https://demoqa.com/links')
            page.open()
            result_expected, result_fact = page.check_new_simple_link()
            assert result_fact == result_expected, "Link is not correct"

        @allure.title('Check broken link')
        def test_check_bad_link(self, driver):
            page = LinkPage(driver, 'https://demoqa.com/links')
            page.open()
            result_expected = 400
            result_fact = page.check_broken_link('https://demoqa.com/bad-request')
            assert result_fact == result_expected, "Link is not correct"

    @allure.feature('Upload and Download')
    class TestUploadAndDownloadPage:
        @allure.title('Upload file')
        def test_upload(self, driver):
            page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            page.open()
            file_name, result = page.upload_file()
            file_name, result = page.upload_file()
            print(file_name)
            print(result)
            assert file_name == result

        @allure.title('Download file')
        def test_download(self, driver):
            page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            page.open()

    @allure.feature('Dynamic elements')
    class TestDynamicElements:
        @allure.title('Dynamic button click')
        def test_click_button(self, driver):
            page = DynamicElementsPage(driver, 'https://demoqa.com/dynamic-properties')
            page.open()
            appear = page.check_click_dynamic_button()
            assert appear, "Button not clickable!"

        @allure.title('Color Change button')
        def test_color_change_button(self, driver):
            page = DynamicElementsPage(driver, 'https://demoqa.com/dynamic-properties')
            page.open()
            before, after = page.check_change_color_button()
            assert before != after, "Color does not change after 5sec"

        @allure.title('Dynamic button visible')
        def test_appear_button(self, driver):
            page = DynamicElementsPage(driver, 'https://demoqa.com/dynamic-properties')
            page.open()
            appear = page.check_visible_dynamic_button()
            assert appear, "Button not visible!"



















































