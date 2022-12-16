from selenium import webdriver
from config import settings

def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress",settings.CHROME_DEBUGGER_ADDRESS)
    options.add_argument("--start-maximized")
    options.add_argument("--user-data-dir=" + settings.CHROME_PROFILE_PATH)
    driver = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_PATH, options=options)
    return driver