from pages.form_page import FormPage


class TestFormPage:
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        print(f'Person: {person}')
        print((f'Result: {result}'))
        assert f"{person.first_name} {person.last_name}" == result[0], "Поля имя и фамилия не заполнено"
        assert person.email == result[1], "форма email не заполнено"





































































