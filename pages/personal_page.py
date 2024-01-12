import allure
import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import smtplib
class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BTN = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")


    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_fild = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            time.sleep(7)

            # first_name_fild.clear()
            # self.driver.find_element(*self.FIRST_NAME_FIELD).clear()

            # clear() для очистки не сработал используем такую конструкцию
            first_name_fild.send_keys(Keys.CONTROL + "A")
            first_name_fild.send_keys(Keys.BACKSPACE)


            assert first_name_fild.get_attribute("value") == '', "The is a text"
            first_name_fild.send_keys(new_name)

            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    @allure.step("Changes has been saved successfuly")
    def is_changes_saved(self):

        # дождемся пока спинет исчезнет
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        # дождемся визуального появления  FIRST_NAME_FIELD
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        # проверка текста
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

