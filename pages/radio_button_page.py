from pages.base_page import BasePage
from locators.radio_button_locators import RadioButtonPageLocators

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()
    def click_rb(self, choice):
        #self.element_is_visible(locators.BUTTON_YES).click()
        choices = {
            'yes':  self.locators.BUTTON_YES,
            'impressive': self.locators.BUTTON_IMPRESSIVE,
            'no': self.locators.BUTTON_NO
                }
        rb = self.element_is_visible(choices[choice])
        rb.click()

    def get_output_result(self):
        return self.element_is_present(self.locators.RESULT).text