import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support import expected_conditions as EC


# Создадим class BasePage в котором
# инициализируем драйвер чтобы он был доступен на всех страницах
# пропишем общие методы для работы со всеми страницами


class BasePage:
    # init то что будет инициализироваться при создании объекта base_pages
    # все аргументы которые указаны в конструкторе
    # будут запрошены в наследуемом классе
    def __init__(self, driver, url):
        self.driver = driver # в тестовых классах будет создавать  объект драйвер
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    # метод который будет открывать страницы
    def open(self):
        with allure.step(f"Open {self.url} page"):
            self.driver.get(self.url)

    # проверяет что запрашиваемая страница открыта
    def is_opened(self):
        with allure.step(f"Page {self.url} is opened"):
            self.wait.until(EC.url_to_be(self.url))

#    метод который позволяет сделать скриншот после каждого теста
    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )



