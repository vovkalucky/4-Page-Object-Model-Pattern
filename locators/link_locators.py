from selenium.webdriver.common.by import By


class LinkPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "#simpleLink")
    BROKEN_LINK = (By.CSS_SELECTOR, "#bad-request")