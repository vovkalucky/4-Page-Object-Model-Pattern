import random
import time

from pages.base_page import BasePage
from locators.browser_window_page_locators import BrowserWinPageLocators
from locators.browser_window_page_locators import AlertLocators
from locators.browser_window_page_locators import FramePageLocators
from locators.browser_window_page_locators import NestedFramePageLocators
from locators.browser_window_page_locators import ModalDialogPageLocators


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

class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_args):
        if frame_args == 1:
            frame = self.element_is_visible(self.locators.FRAME_1)
        if frame_args == 2:
            frame = self.element_is_visible(self.locators.FRAME_2)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.TITLE).text
        self.driver.switch_to.default_content()
        return [text, width, height]

class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    def check_text_in_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_BUTTON).click()
        title = self.element_is_present(self.locators.TITLE_SMALL_MODAL_DIALOG).text
        text = self.element_is_present(self.locators.TEXT_SMALL_MODAL_DIALOG).text
        return title, text

    def check_close_of_modal_dialog(self, close):
        methods_of_close = {
            'cross': self.locators.SMALL_BUTTON_CLOSE_CROSS,
            'button': self.locators.SMALL_BUTTON_CLOSE,
            'dialog_bg': self.locators.DIALOG
            }
        self.element_is_visible(self.locators.SMALL_BUTTON).click()
        result_actual_before_close = self.element_is_present(self.locators.DIALOG).get_attribute('class')
        close_locator = self.element_is_visible(methods_of_close[close])
        close_locator.click()
        result_actual_after_close = self.element_is_present(self.locators.DIALOG).get_attribute('class')
        return result_actual_before_close, result_actual_after_close




