# делаем так чтобы тесты были мультистраничные
#  импортирум все пэйджи
# и используем аннотацию типов python
import pytest
from config.data import Data
from pages.personal_page import PersonalPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    # Создадим фикстуру внутрь прокинем request и driver
    # затем в в самом тесте
    # from base.base_test import BaseTest
    #  и наследуемся от BaseTest
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
