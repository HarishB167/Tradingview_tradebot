import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)        
        
    # Locators
    _account_div = "div.js-account-manager-header > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)"
    
    def get_account_balance(self):
        logging.info("ChartPage.get_account_balance")
        account_div = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self._account_div)))
        balance = float(account_div.text.replace(" ",""))
        print("Account balance : ", balance)
    
    def buy_trade(self):
        pass

    def sell_trade(self):
        pass
        