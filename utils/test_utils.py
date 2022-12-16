

## CODE TO BE USED ##



import time

def log_in(driver, username, password):
    # Navigate to the login page
    driver.get('https://www.example.com/login')

    # Enter the username and password
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)

    # Click the login button
    driver.find_element(By.ID, 'login_button').click()

def wait_for_page_to_load(driver):
    time.sleep(5)

def log_out(driver):
    # Click the logout button
    driver.find_element(By.ID, 'logout_button').click()
    