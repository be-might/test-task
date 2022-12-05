from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObjectClass:

    """
    scroll actions
    """
    def __init__(self):
        self._driver = None
        self._url = None

    def navigate_to_page(self):
        self._driver.get(self._url)

    def find_element(self, element):
        element_obj = WebDriverWait(self._driver, 20)\
            .until(EC.element_to_be_clickable((By.XPATH, element)))
        return element_obj

    def send_keys(self, element, keys):
        self.find_element(element).send_keys(keys)

    def click_element(self, element):
        self.find_element(element).click()

    def switch_to_frame(self, element):
        self._driver.switch_to.frame(self.find_element(element))

    def scroll_to_element(self, element):
        self._driver.execute_script("arguments[0].scrollIntoView();", self.find_element(element))
