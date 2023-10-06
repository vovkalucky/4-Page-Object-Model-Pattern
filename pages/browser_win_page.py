from pages.base_page import BasePage
from locators.browser_window_page_locators import BrowserWinPageLocators


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

