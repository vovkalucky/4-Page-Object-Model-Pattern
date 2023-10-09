import time

from pages.base_page  import BasePage
from locators.dynamic_locators import DynamicLocators

class DynamicElementsPage(BasePage):
    locators = DynamicLocators()

    def check_click_dynamic_button(self):
        try:
            self.element_is_clickable(self.locators.DYNAMIC_5_SEC_BUTTON)
        except TimeoutError:
            return False
        return True

    def check_visible_dynamic_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SEC_BUTTON)
        except TimeoutError:
            return False
        return True

    def check_change_color_button(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after