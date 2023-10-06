from selenium.webdriver.common.by import By



class BrowserWinPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")
    TITLE = (By.CSS_SELECTOR, "#sampleHeading")

class AlertLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "#alertButton")
    ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "#confirmButton")
    CONFIRM_BUTTON_RESULT = (By.CSS_SELECTOR, "#confirmResult")
    PROMPT_BUTTON = (By.CSS_SELECTOR, "#promtButton")
    PROMPT_BUTTON_RESULT = (By.CSS_SELECTOR, "#promptResult")