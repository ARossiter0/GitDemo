from selenium.webdriver.common.by import By


class ConfirmPage:
    country_search = (By.ID, "country")
    terms_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_button = (By.XPATH, "//input[@type='submit']")
    success_text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def get_country_search(self):
        return self.driver.find_element(*ConfirmPage.country_search)

    def get_dropdown_link(self, link_text):
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def accept_terms(self):
        self.driver.find_element(*ConfirmPage.terms_checkbox).click()

    def click_submit(self):
        self.driver.find_element(*ConfirmPage.submit_button).click()

    def get_success_text(self):
        return self.driver.find_element(*ConfirmPage.success_text).text
