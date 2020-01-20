from selenium import webdriver
from resources.data.constant_variables import *
#from sources.pages.utilities.generic_methods import implicitlyWait

class WebDriverFactory():
    def __init__(self, driver):
        self.driver = driver

    def getWebDriverInstance(self):
        if self.driver == "firefox":
            driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
        elif self.driver == "ie":
            driver = webdriver.Ie(executable_path=IE_PATH)
        else:
            driver = webdriver.Chrome(executable_path=CHROME_PATH)
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(20)
        return driver


