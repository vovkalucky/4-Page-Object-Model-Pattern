from pages.base_page import BasePage
from locators.buttonpage_locators import ButtonPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    def double_click_on_button(self, driver):
        action_chains = ActionChains(driver)
        element_to_double_click = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        action_chains.double_click(element_to_double_click).perform()

    def check_double_click_on_button(self):
        return self.element_is_present(self.locators.DOUBLE_CLICK_BUTTON_MESSAGE).text

    def click_on_button(self):
        self.element_is_visible(self.locators.CLICK_BUTTON).click()


    def check_click_on_button(self):
        return self.element_is_present(self.locators.CLICK_BUTTON_MESSAGE).text

    def right_click_on_button(self, driver):
        action_chains = ActionChains(driver)
        element_to_click = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        action_chains.context_click(element_to_click).perform()
        self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON).click()


    def check_right_click_on_button(self):
        return self.element_is_present(self.locators.RIGHT_CLICK_BUTTON_MESSAGE).text
