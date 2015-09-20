from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/ ')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    keyone = randint(0, 3)
    if keyone == 0:
        htmlElem.send_keys(Keys.UP)
    elif keyone == 1:
        htmlElem.send_keys(Keys.RIGHT)
    elif keyone == 2:
        htmlElem.send_keys(Keys.DOWN)
    elif keyone == 3:
        htmlElem.send_keys(Keys.LEFT)