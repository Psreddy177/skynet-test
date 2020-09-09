from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self, driver):
        self.driver =driver

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_xpath("//img[@alt='Lougout']")
        except:
            return None

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(driver=self.driver, timeout=30)
        wait.until(expected_conditions.visibility_of(self.get_logout_button()))