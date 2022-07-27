import pytest
from pages.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_homepage(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)

        # ID, Xpath, CSSSelector, Classname, name, linktext, text
        home_page.get_name().send_keys(get_data["firstname"])
        log.info("First name: " + get_data["firstname"])
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_password().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        home_page.get_radio().click()

        # Static dropdown
        self.select_option_by_text(home_page.get_dropdown(), get_data["gender"])

        home_page.get_submit().click()
        msg = home_page.get_alert().text
        assert "Success" in msg

        home_page.get_bindingbox().send_keys("Hello again")
        home_page.get_bindingbox().clear()
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data())
    def get_data(self, request):
        return request.param
