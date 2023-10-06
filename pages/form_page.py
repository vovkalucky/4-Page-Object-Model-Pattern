import os
import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as locators
from generator.generator import generated_person
from generator.generator import generated_file
class FormPage(BasePage):
    def remove_footer(self):

        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove()')
    def fill_fields_and_submit(self):
        # first_name = 'Ivan'
        # last_name = 'Petrov'
        # email = 'hello@mail.ru'
        person = generated_person()
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(locators.EMAIL).send_keys(person.email)
        self.element_is_visible(locators.GENDER).click()
        self.element_is_visible(locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(locators.SUBJECT)
        print(person.subject)
        for item in person.subject:
            subject.send_keys(f"{item}")
            subject.send_keys(Keys.RETURN)
        self.element_is_visible(locators.HOBBIES).click()
        self.element_is_visible(locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(locators.CURRENT_ADDRESS).send_keys(person.current_address)
        #self.element_is_visible(locators.DATE_OF_BIRTH).send_keys(person.date_of_birth)
        self.element_is_visible(locators.SELECT_STATE).click()
        self.element_is_visible(locators.SELECT_STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(locators.SELECT_CITY).click()
        self.element_is_visible(locators.SELECT_CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        print(result_text)
        return result_text




