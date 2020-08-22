from unittest import TestCase

from lib.ui.login_page import LoginPage
from lib.utils import create_driver

class TestSample(TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_sample(self):
        self.login_page.wait_for_login_page_to_load()
        title = self.driver.title
        assert title == 'actitime - Login'
