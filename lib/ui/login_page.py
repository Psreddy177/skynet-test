from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage
    def __init__(self, driver):
        self.driver = driver

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_name('username')
        except:
            return None

    def get_password_testbox(self):
        try:
            return self.driver.find_element_by_name('pwd')
        except:
            return None

    def get_loggin_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Username or Password is invalid. please try again']")
        except:
            return None

        def wait_for_login_page_to_load(self):
            wait = WebDriverWait(timeout=30, driver=self.driver)
            wait.until(expected_conditions.visibility_of(self.get_username_testbox()))
            wait.until(expected_conditions.visibility_of(self.get_password_testbox()))
            wait.until(expected_conditions.visibility_of(self.get_login_button()))
