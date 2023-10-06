import random
import time
import allure
import pytest
from pages.browser_win_page import BrowserWinPage
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
