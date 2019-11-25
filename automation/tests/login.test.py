from selenium import webdriver
import time
import unittest


class LoginTest(unittest.TestCase):
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="Users/anhmai/download/chromedriver")
