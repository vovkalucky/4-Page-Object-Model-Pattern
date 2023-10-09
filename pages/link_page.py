import requests

from pages.base_page import BasePage
from locators.link_locators import LinkPageLocators

class LinkPage(BasePage):
    locators = LinkPageLocators()

    def check_new_simple_link(self):
        link = self.element_is_visible(self.locators.SIMPLE_LINK)
        result_expected = link.get_attribute('href')
        #print(result_expected)
        request = requests.get(result_expected)
        if request.status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            result_fact = self.driver.current_url
            #print(result_expected)
            return result_expected, result_fact
        else:
            return result_expected, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.BROKEN_LINK).click()
        else:
            return request.status_code




