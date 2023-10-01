from selenium.webdriver.common.by import By



class ButtonPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    DOUBLE_CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")

    #CLICK_BUTTON = (By.LINK_TEXT, "Click Me")
    CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")

    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    RIGHT_CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")