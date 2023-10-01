from selenium.webdriver.common.by import By



class WebtableLocators:
    #add new person
    BUTTON_ADD = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    AGE = (By.CSS_SELECTOR, '#age')
    SALARY = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT = (By.CSS_SELECTOR, '#department')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    #check table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    #search person
    SEARCH = (By.CSS_SELECTOR, '#searchBox')
    DELETE = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'

    # edit person
    BUTTON_EDIT = (By.CSS_SELECTOR, 'span[title="Edit"]')
    AGE_EDIT = (By.CSS_SELECTOR, '#age')
    SUBMIT_EDIT = (By.CSS_SELECTOR, '#submit')

    #delete person
    NO_DATA = (By.CSS_SELECTOR, 'div[class="rt-noData"]')

    #change count rows
    SELECT_ROWS = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

