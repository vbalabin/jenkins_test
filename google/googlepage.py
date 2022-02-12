from google.locators import CalculatorLocators, GoogleLocators
from google.basepage import BasePage


class GoogleBase(GoogleLocators, CalculatorLocators, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_calc()
        return

    def go_to_calc(self):
        """
        info: goes to google.com calculator
        """     
        self.enter_text(self.MAIN_INPUT, 'калькулятор')
        self.click(self.SEARCH_BUTTON)


    def get_memory_value(self):
        """
        return: str
        info: gets google.com calculator memory field value
        """
        return self.get_text(self.FIELD_MEMORY)

    def get_result_value(self):
        """
        return: str
        info: gets google.com calculator result field value
        """     
        return self.get_text(self.FIELD_RESULT)        


class GoogleAlgebraic(GoogleBase):
    def __init__(self, driver):
        super().__init__(driver)
        return

    def perform_actions_01(self):
        """
        info: clicks (1 + 2) × 3 - 40 ÷ 5 =
        """
        self.click(self.SYM_LEFT_PAR)
        self.click(self.NUM_1)
        self.click(self.SYM_ADD)
        self.click(self.NUM_2)
        self.click(self.SYM_RIGHT_PAR)
        self.click(self.SYM_MUL)
        self.click(self.NUM_3)
        self.click(self.SYM_SUB)
        self.click(self.NUM_4)
        self.click(self.NUM_0)
        self.click(self.SYM_DIV)
        self.click(self.NUM_5)
        self.click(self.SYM_EQUALS)
    

class GoogleZeroDiv(GoogleBase):
    def __init__(self, driver):
        super().__init__(driver)


    def perform_actions_02(self):
        """
        info: clicks 6 ÷ 0 =
        """
        self.click(self.NUM_6)
        self.click(self.SYM_DIV)
        self.click(self.NUM_0)
        self.click(self.SYM_EQUALS)


class GoogleEmpty(GoogleBase):
    def __init__(self, driver):
        super().__init__(driver)


    def perform_actions_03(self):
        """
        info: clicks sin
        """
        self.click(self.SYM_SIN)
        self.click(self.SYM_EQUALS)
        return