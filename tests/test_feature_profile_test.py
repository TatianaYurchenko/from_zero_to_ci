import random
import time
import allure
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage
#  дает мультистраничный доступ
@allure.feature("Profile functionality")
class TestProfileFeature:

    @allure.title("Change profile name")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_change_profile_name(self, driver):
        page = LoginPage(driver, url=LoginPage.PAGE_URL)
        page2 = DashboardPage(driver, url=DashboardPage.PAGE_URL)
        page3 = PersonalPage(driver, url=PersonalPage.PAGE_URL)
        page.open()
        page.is_opened()
        page.enter_login('Admin')
        page.enter_password('admin123')
        page.click_submit_btn()
        page2.is_opened()
        page2.click_my_info_link()
        page3.is_opened()
        page3.change_name(f"Test {random.randint(1, 100)}")
        page3.save_changes()
        page3.is_changes_saved()
        page3.make_screenshot("Success")

