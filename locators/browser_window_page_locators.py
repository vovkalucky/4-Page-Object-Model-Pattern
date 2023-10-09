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

class FramePageLocators:
    FRAME_1 = (By.CSS_SELECTOR, "#frame1")
    FRAME_2 = (By.CSS_SELECTOR, "#frame2")
    TITLE = (By.CSS_SELECTOR, "#sampleHeading")

class NestedFramePageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "#frame1")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")

class ModalDialogPageLocators:
    SMALL_BUTTON = (By.CSS_SELECTOR, "#showSmallModal")
    SMALL_BUTTON_CLOSE = (By.CSS_SELECTOR, "#closeSmallModal")
    SMALL_BUTTON_CLOSE_CROSS = (By.CSS_SELECTOR, ".close")
    SHOW_MODAL_CLOSE = (By.CSS_SELECTOR, ".fade modal")
    SHOW_MODAL = (By.CSS_SELECTOR, ".fade modal show")
    DIALOG = (By.CSS_SELECTOR, "div[role='dialog']")

    TITLE_SMALL_MODAL_DIALOG = (By.CSS_SELECTOR, "#example-modal-sizes-title-sm")
    TEXT_SMALL_MODAL_DIALOG = (By.CSS_SELECTOR, ".modal-body")
