from selenium.webdriver.common.by import By


class GoogleLocators(object):
    """
    for google.com
    """
    MAIN_INPUT = (By.XPATH, r'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    SEARCH_BUTTON = (By.XPATH, r'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')


class CalculatorLocators(object):
    """
    for google calculator
    """
    FIELD_MEMORY = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span')
    FIELD_RESULT = (By.XPATH, r'//*[@id="cwos"]')
    NUM_0 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[1]/div/div')
    NUM_1 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
    NUM_2 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
    NUM_3 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')
    NUM_4 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[1]/div/div')
    NUM_5 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div')
    NUM_6 = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[3]/div/div')
    SYM_LEFT_PAR = (By.XPATH,  r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[1]/div/div')
    SYM_RIGHT_PAR = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[2]/div/div')
    SYM_EQUALS = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')
    SYM_ADD = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')
    SYM_SUB = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')
    SYM_MUL = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
    SYM_DIV = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[4]/div/div')
    SYM_SIN = (By.XPATH, r'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[1]/tbody/tr[2]/td[2]/div/div[1]')

    