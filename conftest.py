import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# фикстиура которая будет инициализировать драйвер для тестов
# request параметр который позволяет создавать объект драйвера внутри пэджей и внутри тестов
# будет втоматом вызываться для каждого теста, экземпляр браузера будет создаваться для каждого теста
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--incognito")
    # options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver # создает объект драйвера внутри тестовых классов
    yield driver
    driver.quit()
