import allure
import pytest

from pages.browser_win_page import BrowserWinPage
from pages.browser_win_page import AlertPage
from pages.browser_win_page import FramePage
from pages.browser_win_page import NestedFramePage
from pages.browser_win_page import ModalDialogPage
@allure.suite("Alerts Frame Window")
class TestAlertsFrameWindow:
    @allure.feature('BrowserWinPage')
    class TestBrowserWinPage:
        @allure.title('Check New Tab')
        def test_new_tab(self, driver):
            page = BrowserWinPage(driver, 'https://demoqa.com/browser-windows')
            page.open()
            result_actual = page.check_opened_new_tab()
            result_expect = "This is a sample page"
            assert result_actual == result_expect, "Text in New Tab does not match expected"

    @allure.feature('AlertPage')
    class TestAlerts:
        @allure.title('Check New Window')
        def test_new_window(self, driver):
            page = BrowserWinPage(driver, 'https://demoqa.com/browser-windows')
            page.open()
            result_actual = page.check_opened_window()
            result_expect = "This is a sample page"
            assert result_actual == result_expect, "Text in New Window does not match expected"

        @allure.title('Check Alert')
        def test_alert(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_actual = page.check_alert()
            result_expect = "You clicked a button"
            assert result_actual == result_expect, "Text in Alert does not match expected"

        @allure.title('Check Alert after 5 sec')
        def test_alert_after_5_Sec(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_actual = page.check_alert_after_5_Sec()
            result_expect = "This alert appeared after 5 seconds"
            assert result_actual == result_expect, "Text in Alert does not match expected"

        @allure.title('Check Confirm')
        def test_confirm(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_fact = page.check_confirm()
            result_expect = "You selected Ok"
            assert result_fact == result_expect, "Text in Confirm does not match expected"

        @allure.title('Check User Text in Prompt')
        def test_prompt(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_expect, result_actual = page.check_prompt()
            result_actual = result_actual.split("entered ")[1]
            assert result_actual == result_expect, "Text in Prompt does not match expected"

    @allure.feature('FramePage')
    class TestFrames:
        @allure.title('Check Frame_1')
        def test_frame(self, driver):
            page = FramePage(driver, 'https://demoqa.com/frames')
            page.open()
            result_actual = page.check_frame(1)[0]
            result_expect = "This is a sample page"
            assert result_actual == result_expect, "Text in Frame does not match expected"

        @allure.title('Check Frame_2')
        def test_text_in_frame(self, driver):
            page = FramePage(driver, 'https://demoqa.com/frames')
            page.open()
            result_actual = page.check_frame(2)[0]
            result_expect = "This is a sample page"
            assert result_actual == result_expect, "Text in Frame does not match expected"

        @allure.title('Check Frame_1 size')
        def test_size_of_frame(self, driver):
            page = FramePage(driver, 'https://demoqa.com/frames')
            page.open()
            result_actual_width = page.check_frame(1)[1]
            result_actual_height = page.check_frame(1)[2]
            result_expect_width = "500px"
            result_expect_height = "350px"
            assert result_actual_width == result_expect_width and result_actual_height == result_expect_height, "Size of Frame_1 does not match expected"

        @allure.title('Check Frame_2 size')
        def test_size_of_frame(self, driver):
            page = FramePage(driver, 'https://demoqa.com/frames')
            page.open()
            result_actual_width = page.check_frame(2)[1]
            result_actual_height = page.check_frame(2)[2]
            result_expect_width = "100px"
            result_expect_height = "100px"
            assert result_actual_width == result_expect_width and result_actual_height == result_expect_height, "Size of Frame_2 does not match expected"

    @allure.feature('NestedFramePage')
    class TestNestedFrames:
        @allure.title('Check NestedFrame')
        def test_nested_frame(self, driver):
            page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            page.open()
            result_actual_parent, result_actual_child = page.check_nested_frame()
            result_expect_parent = "Parent frame"
            result_expect_child = "Child Iframe"
            assert result_actual_parent == result_expect_parent, "Text in Parent Frame does not match expected"
            assert result_actual_child == result_expect_child, "Text in Child Frame does not match expected"

    @allure.feature('ModalDialogPage')
    class TestModalDialogs:
        @allure.title('Check Text ModalDialog')
        def test_text_modal_dialog(self, driver):
            page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            page.open()
            result_actual_title, result_actual_text = page.check_text_in_modal_dialog()
            result_expect_title = "Small Modal"
            result_expect_text = "This is a small modal. It has very less content"
            assert result_actual_title == result_expect_title, "Title in Modal Window does not match expected"
            assert result_actual_text == result_expect_text, "Text in Modal Window does not match expected"

        @pytest.mark.parametrize('close', ["cross", "button", "dialog_bg"])
        @allure.title('Check Close ModalDialog')
        def test_close_modal_dialog(self, driver, close):
            page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            page.open()
            result_actual_before_close, result_actual_after_close = page.check_close_of_modal_dialog(close)
            result_expect_before_close, result_expect_after_close = "fade modal show", "fade modal"
            assert result_expect_before_close == result_actual_before_close, "Modal Window does not close"
            assert result_expect_after_close == result_actual_after_close, "Modal Window does not close"
