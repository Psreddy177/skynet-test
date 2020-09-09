import json
from unittest import TestCase

from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.utils import create_driver

class TestLoginS13570(TestCase):
    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()
    def test_login_valid_tc12323(self):
        data= json.load(open('./test/regression/login/S13570.json'))

        self.login_page.wait_for_login_page_to_load()
        self.login_page.get_username_textbox().send_keys(data['TC12323'] ['username'])
        self.login_page.get_password_testbox().send_keys(data['TC12323'] ['password'])
        self.login_page.get_loggin_button().click()
        self.home_page.wait_for_home_page_to_load()
        actual_title = self.driver.title
        assert actual_title = data['TC12323'] ['home_page_title']
        logout_link_status = self.home_page.get_logout_button().is_enabled()
        assert logout_link_status == True
        self.home_page.get_logout_button().click

        self.login_page.wait_for_login_page_to_load()


