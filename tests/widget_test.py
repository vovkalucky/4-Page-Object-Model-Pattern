import allure
from pages.widget_page import AccordeonPage
@allure.suite("Widget")
class TestWidget:
    @allure.feature('Accordeon')
    class TestAccordeon:
        @allure.title('Check Accordeon')
        def test_accordeon(self, driver):
            page = AccordeonPage(driver, 'https://demoqa.com/accordian')
            page.open()
            first_title, first_content = page.check_accordeon('first')
            second_title, second_content = page.check_accordeon('second')
            third_title, third_content = page.check_accordeon('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

