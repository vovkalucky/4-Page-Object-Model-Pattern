import random
import time
import allure
import pytest
from pages.browser_win_page import BrowserWinPage
from pages.browser_win_page import AlertPage
@allure.suite("Alerts Frame Window")
class TestElements:
    @allure.feature('BrowserWinPage')
    class TestBrowserWinPage:
        @allure.title('Check New Tab')
        def test_new_tab(self, driver):
            page = BrowserWinPage(driver, 'https://demoqa.com/browser-windows')
            page.open()
            result_fact = page.check_opened_new_tab()
            result_expect = "This is a sample page"
            assert result_fact == result_expect, "Text in New Tab not right"

        @allure.title('Check New Window')
        def test_new_window(self, driver):
            page = BrowserWinPage(driver, 'https://demoqa.com/browser-windows')
            page.open()
            result_fact = page.check_opened_window()
            result_expect = "This is a sample page"
            assert result_fact == result_expect, "Text in New Window not right"

        @allure.title('Check Alert')
        def test_alert(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_fact = page.check_alert()
            result_expect = "You clicked a button"
            assert result_fact == result_expect, "Text in Alert not right"

        @allure.title('Check Alert after 5 sec')
        def test_alert_after_5_Sec(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_fact = page.check_alert_after_5_Sec()
            result_expect = "This alert appeared after 5 seconds"
            assert result_fact == result_expect, "Text in Alert not right"

        @allure.title('Check Confirm')
        def test_confirm(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_fact = page.check_confirm()
            result_expect = "You selected Ok"
            assert result_fact == result_expect, "Text in Confirm not right"

        @allure.title('Check User Text in Prompt')
        def test_prompt(self, driver):
            page = AlertPage(driver, 'https://demoqa.com/alerts')
            page.open()
            result_expect, result_actual = page.check_prompt()
            result_actual = result_actual.split("entered ")[1]
            assert result_actual == result_expect, "Text in Prompt not right"
