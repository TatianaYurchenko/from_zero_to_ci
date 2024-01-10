from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import smtplib
class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BTN = ("xpath", "(//button[@type='submit'])[1]")

    def change_name(self, new_name):
        first_name_fild = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
        first_name_fild.clear()
        assert first_name_fild.get_attribute("value") == '', "The is a text"
        first_name_fild.send_keys(new_name)
        self.name = new_name
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

