from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.widget_page_locators import AccordeonPageLocators

class AccordeonPage(BasePage):
    locators = AccordeonPageLocators()
    def check_accordeon(self, num):
        accordeon = {'first': {'title': self.locators.SECTION_FIRST,
                               'content': self.locators.SECTION_CONTENT_FIRST},
                     'second': {'title': self.locators.SECTION_SECOND,
                                'content': self.locators.SECTION_CONTENT_SECOND},
                     'third': {'title': self.locators.SECTION_THIRD,
                               'content': self.locators.SECTION_CONTENT_THIRD}
                     }
        section_title = self.element_is_visible(accordeon[num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordeon[num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordeon[num]['content']).text
        return [section_title.text, len(section_content)]

