from argparse import ArgumentParser
from selenium.webdriver import Chrome,Firefox,Ie

def get_browser_instance():

    parser = ArgumentParser()
    parser.add_argument('--browser', default='chrome')
    parser.add_argument('--url', default='test')
    parser.add_argument('--env', default='windows')

    options, args = parser.parse_known_args()
    browser_type = options.browser.lower()
    url_info = options.url.lower()
    env_info = options.env.lower()

    if browser_type == 'chrome':
        driver = Chrome("E:\PY\PycharmProjects\skynet-test\browser-severs\chromedriver.exe")
    elif browser_type == 'firefox':
        driver = Firefox("./browser-severs/geckodrivers.exe")
    else:
        print('!!!!!!======== Invalid browser option check command line =====!!!!!!!')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)

    if url_info != 'prod':
        driver.get('http://localhost/login.jsp')
    else:
        driver.get('https://demo.actitime.com/login.do')
    return None