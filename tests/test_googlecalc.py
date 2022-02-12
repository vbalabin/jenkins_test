import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType
import google.googlepage as gp
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestGoogleCalc():
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME.copy(),
            options=chrome_options
        )
        self.driver.get("http://www.google.com")

        yield
        self.driver.quit()


    @allure.feature("001 тест")
    @allure.story("Проверка операций с целыми числами")
    def test_001_algebraic_integers(self):
        """
        info: Проверка операций с целыми числами
        """
        test_obj = gp.GoogleAlgebraic(self.driver)
        test_obj.perform_actions_01()
        with allure.step('скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='testscr', attachment_type=AttachmentType.PNG)
        assert test_obj.get_memory_value() == '(1 + 2) × 3 - 40 ÷ 5 =', 'memory value has failed'
        assert test_obj.get_result_value() == '1', 'result value test has failed'

    @allure.feature("002 тест")
    @allure.story("Проверка деления на ноль")
    def test_002_zero_div(self):
        """
        info: Проверка деления на ноль
        """
        test_obj = gp.GoogleZeroDiv(self.driver)
        test_obj.perform_actions_02()
        with allure.step('скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='testscr', attachment_type=AttachmentType.PNG)
        assert test_obj.get_memory_value() == '6 ÷ 0 =', 'memory value has failed'
        assert test_obj.get_result_value() == 'Infinity', 'result value test has failed'

    @allure.feature("003 тест")
    @allure.story("Проверка ошибки при отсутствии значения")
    def test_003_empty_input(self):
        """
        info: Проверка ошибки при отсутствии значения
        """
        with allure.step('скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='testscr', attachment_type=AttachmentType.PNG)        
        test_obj = gp.GoogleEmpty(self.driver)
        test_obj.perform_actions_03()        
        assert test_obj.get_memory_value() == 'sin() =', 'memory value has failed'
        assert test_obj.get_result_value() == 'Error', 'result value test has failed' 
