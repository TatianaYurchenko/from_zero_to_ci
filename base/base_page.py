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
        self.driver.get(self.PAGE_URL)

    # проверяет что запрашиваемая страница открыта
    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))



