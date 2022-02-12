from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    used as base page for testing google calc
    """

    def __init__(self, driver, timer=10):
        self.driver = driver
        self.timer = timer

    def click(self, by_locator):
        """
        param: by_locator
        type: tuple(selenium By, str)
        return: selenium element
        info: finds and clicks
        """        
        element = WebDriverWait(self.driver, self.timer).until(EC.visibility_of_element_located(by_locator))
        element.click()
        return element

    def get_text(self, by_locator):
        """
        param: by_locator
        type: tuple(selenium By, str)
        return: str
        info: gets an element text value
        """  
        element = WebDriverWait(self.driver, self.timer).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def enter_text(self, by_locator, text):
        """
        param: by_locator
        type: tuple(selenium By, str)
        return: selenium element
        info: send text to an element
        """
        element = WebDriverWait(self.driver, self.timer).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)
        return element