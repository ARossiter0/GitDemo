from selenium.webdriver.common.by import By

from pages.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert_success = (By.CLASS_NAME, "alert-success")
    binding_box = (By.XPATH, "(//input[@type='text'])[3]")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_radio(self):
        return self.driver.find_element(*HomePage.radio)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert_success)

    def get_bindingbox(self):
        return self.driver.find_element(*HomePage.binding_box)
