from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytest import ExitCode
import time

username = "YOUR EMAIL"
password = "YOUR PASSWORD"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

emailElement = driver.find_element_by_id()
emailElement.send_keys(username)

passwordElement = driver.find_element_by_id('passwordid')
passwordElement.send_keys()
print(driver.title)  # return the title of the page
print(driver.current_url)  # return the current url of the page

time.sleep(5)
