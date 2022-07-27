import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # File handler object
        logger.setLevel(logging.INFO)
        return logger
