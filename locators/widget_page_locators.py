from selenium.webdriver.common.by import By


class AccordeonPageLocators():
    SECTION_FIRST = (By.CSS_SELECTOR, '#section1Heading')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, '#section1Content p')
    SECTION_SECOND = (By.CSS_SELECTOR, '#section2Heading')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, '#section2Content p')
    SECTION_THIRD = (By.CSS_SELECTOR, '#section3Heading')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, '#section3Content p')
