from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)        
        
    # Locators
    _search_box = "button.tv-header-search-container"
    _search_input = "input[name=query]"    
    
    def enter_search_term(self, search_term):
        search_bar = self.driver.find_element_by_css_selector(self._search_box)
        search_bar.click()        
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self._search_input)))
        search_input.send_keys(search_term)

    def do_search(self):
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self._search_input)))
        search_input.send_keys(Keys.ENTER)
        