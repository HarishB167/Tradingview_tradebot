## CODE TO BE USED ##

from selenium.webdriver.common.by import By

def click_element(driver, locator):
    element = driver.find_element(locator)
    element.click()

def enter_text(driver, locator, text):
    element = driver.find_element(locator)
    element.clear()
    element.send_keys(text)

def get_text(driver, locator):
    element = driver.find_element(locator)
    return element.text

def is_element_present(driver, locator):
    elements = driver.find_elements(locator)
    return len(elements) > 0

