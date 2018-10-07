from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from common.decorator.singleton import Singleton

class FirefoxDriver(metaclass=Singleton):
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("javascript.enabled", True)
        driver = webdriver.Firefox(profile)

        self.driver = driver

    def driver(self):
        return self.driver
