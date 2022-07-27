from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self, setup):
        log = self.get_logger()
        # Home Page
        home_page = HomePage(self.driver)

        # Checkout Page
        checkout_page = home_page.shop_items()
        cards = checkout_page.get_cards()
        log.info("Getting all the card titles")
        for card in cards:
            product_name = checkout_page.get_card_title(card)
            if product_name == "Blackberry":
                checkout_page.get_card_button(card).click()
                break
        checkout_page.get_shop_checkout_button().click()

        # Confirm Page
        confirm_page = checkout_page.go_confirm()
        confirm_page.get_country_search().send_keys("ind")
        log.info("Entering country name 'ind'")
        self.verify_link_presence("India")
        confirm_page.get_dropdown_link("India").click()
        confirm_page.accept_terms()
        confirm_page.click_submit()
        success_text = confirm_page.get_success_text()
        log.info("Text received from application: " + success_text)
        assert "Success! Thank you!" in success_text

        self.driver.get_screenshot_as_file("screen.png")
