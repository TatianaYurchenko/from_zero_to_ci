import allure
# все пэйджи мы будем наследовать от BasePage чтобы все методы из BasePage были доступны
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE


    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BTM = ("xpath", "//button[@type='submit']")

    # шаги. прописываем шаги для взаимодействия с элементами на странице
    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTM)).click()

