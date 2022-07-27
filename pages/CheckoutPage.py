from selenium.webdriver.common.by import By

from pages.ConfirmPage import ConfirmPage


class CheckoutPage:
    cards = (By.XPATH, "//div[@class='card h-100']")
    card_title = (By.XPATH, "div/h4/a")
    card_button = (By.XPATH, "div/button")
    shop_checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    cart_checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def get_cards(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def get_card_title(self, card):
        return card.find_element(*CheckoutPage.card_title).text

    def get_card_button(self, card):
        return card.find_element(*CheckoutPage.card_button)

    def get_shop_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.shop_checkout_button)

    def go_confirm(self):
        self.driver.find_element(*CheckoutPage.cart_checkout_button).click()
        return ConfirmPage(self.driver)
