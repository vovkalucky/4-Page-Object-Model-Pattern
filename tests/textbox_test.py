import time

from pages.textbox_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, "Fullname does not match!"
            assert email == output_email, "Email does not match!"
            assert current_address == output_cur_address, "Current address does not match!"
            assert permanent_address == output_per_address, "Permanent address does not match!"


































