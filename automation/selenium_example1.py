from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = "YOUR EMAIL"
password = "YOUR PASSWORD"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

emailElement = driver.find_element_by_id()
emailElement.send_keys(username)

passwordElement = driver.find_element_by_id('passwordid')
passwordElement.send_keys()
