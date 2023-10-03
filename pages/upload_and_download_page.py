import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.upload_and_download_page_locators import UploadAndDownloadPageLocators
from generator.generator import generated_file

class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOAD_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]