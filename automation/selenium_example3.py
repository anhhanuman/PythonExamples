import unittest

from selenium.webdriver.firefox import webdriver  # what is the difference?
from selenium import webdriver
import time


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit())

    def testPageTitle(self):
        self.browser.get('http:google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
