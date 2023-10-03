from selenium.webdriver.common.by import By


class DynamicLocators:
    DYNAMIC_5_SEC_BUTTON = (By.CSS_SELECTOR, '#enableAfter')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, '#colorChange')
    VISIBLE_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, '#visibleAfter')