from sources.utilities.webdriver_factory import *
from sources.pages.loginPage import login

from vtiger_framework.sources.utilities.webdriver_factory import WebDriverFactory


class HomeVtigerLogin(WebDriverFactory):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def loginToApp(self):
        login(self.driver).login_to_application("admin","root")
