import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers import chrome
from config import settings
from pages.home_page import HomePage

class TestLogin(unittest.TestCase):
    def setUp(self):        
        self.driver = chrome.get_chrome_driver()
        
        
    def test_login(self):
        self.driver.get(settings.BASE_URL)
        
        home_page = HomePage(self.driver)
        home_page.enter_search_term('NSE:RELIANCE')
        home_page.do_search()
        # self.assertTrue(login_form.is_displayed())
        
    def tearDown(self):
        # Close the web driver
        # self.driver.close()
        pass