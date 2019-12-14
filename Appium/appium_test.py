import unittest
from appium import webdriver
import os
import time
import xml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': '/app.zip',
                'platformName': 'iOS',
                'deviceName': 'iPhone Simulator',
                'automationName': 'XCUITest',
            },
            direct_connection=True
        )

    def tearDown(self):
        self.driver.quit()

    def _get(self, text, index=None, partial=False):
        selector = "name"
        if text.startswitch('#'):
            elements = self.driver.find_elements_by_accessibility_id(text[1:])
        else:
            elements = self.driver.find_elements_by_xpath('//*[@%s="%s"]' % (selector, text))

    def wait_until(self):
        search_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia")))
        search_element.click()
        return self._get()
