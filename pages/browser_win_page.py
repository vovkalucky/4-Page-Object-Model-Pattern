import random
import time

from pages.base_page import BasePage
from locators.browser_window_page_locators import BrowserWinPageLocators
from locators.browser_window_page_locators import AlertLocators


class BrowserWinPage(BasePage):
    locators = BrowserWinPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_visible(self.locators.TITLE).text
        return title_text

    def check_opened_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_visible(self.locators.TITLE).text
        return title_text

class AlertPage(BasePage):
    locators = AlertLocators()

    def check_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text

    def check_alert_after_5_Sec(self):
        self.element_is_visible(self.locators.ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text

    def check_confirm(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_BUTTON_RESULT).text
        return text_result

    def check_prompt(self):
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        prompt = self.driver.switch_to.alert
        input_text = f"My answer{random.randint(0,999)}"
        prompt.send_keys(input_text)
        prompt.accept()
        text_result = self.element_is_visible(self.locators.PROMPT_BUTTON_RESULT).text
        return input_text, text_result


