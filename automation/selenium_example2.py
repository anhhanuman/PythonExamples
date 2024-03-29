# https://pypi.org/project/selenium/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://selenium.org')
assert 'Yahoo' in browser.title
elem = browser.find_element_by_name('p')
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()


def test_basic_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'

    browser.get(URL)
