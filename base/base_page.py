import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Создадим class BasePage в котором
# инициализируем драйвер чтобы он был доступен на всех страницах
# пропишем общие методы для работы со всеми страницами


class BasePage:
    # init то что будет инициализироваться при создании объекта base_pages
    # все аргументы которые указаны в конструкторе
    # будут запрошены в наследуемом классе
    def __init__(self, driver):
        self.driver = driver # в тестовых классах будет создавать  объект драйвер
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    # метод который будет открывать страницы
    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    # проверяет что запрашиваемая страница открыта
    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

#    метод который озволяет сделать скриншот после каждого теста
    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )



