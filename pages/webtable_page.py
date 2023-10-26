
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.webtable_locators import WebtableLocators
from generator.generator import generated_person

class WebtablePage(BasePage):
    locators = WebtableLocators()

    def add_person(self):
        person = generated_person()
        first_name = person.first_name
        last_name = person.last_name
        email = person.email
        age = person.age
        salary = person.salary
        department = person.department
        self.element_is_visible(self.locators.BUTTON_ADD).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH).send_keys(keyword)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        #row = self.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):

        #rand = random.randint(0, len(edit_buttons)-1)
        # person_edit = edit_buttons[rand]
        # person_edit.click()
        person = generated_person()
        #age = random.randint(18, 100)
        age = person.age
        self.element_is_visible(self.locators.BUTTON_EDIT).click()
        self.element_is_visible(self.locators.AGE_EDIT).clear()
        self.element_is_visible(self.locators.AGE_EDIT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_EDIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE).click()

    def check_delete(self):
        return self.element_is_present(self.locators.NO_DATA).text

    def select_change_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.SELECT_ROWS)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        print('\nRemove Footer')

    def remove_fixedban(self):
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")
        print('\nRemove Fixedban')





