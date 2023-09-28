from selenium.webdriver.common.by import By


class RadioButtonPageLocators:
    BUTTON_YES = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    BUTTON_NO = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    # BUTTON_YES = (By.CSS_SELECTOR, '#yesRadio')
    # BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, '#impressiveRadio')
    # BUTTON_NO = (By.CSS_SELECTOR, '#noRadio')
    RESULT = (By.CSS_SELECTOR, '.text-success')