from automation.locators import LoginLocator
from selenium import webdriver


class Login:
    def __init__(self, driver):
        self.driver = driver

    def inputUsername(self):
# send user name test data to the username object
