import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebdriverPythonBasics(unittest.TestCase):


def setUp(self):
    self.browser = webdriver.Firefox()


def test_saucelabs_homepage_header_displayed(self):
    self.browser.get("https:www.saucelabs.com")
    element = self.browser.find_element(By.XPATH, '//a[text()="Platforms"]')
