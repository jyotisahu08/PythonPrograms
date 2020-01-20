"""
Used for logging in to the application
"""
from sources.utilities.generic_methods import *
from sources.utilities import custom_logger as cl


class login(GenericMethods):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_to_application(self, name, password):
        self.sendKeys(name, "user_name", "name")
        self.sendKeys(password, "user_password", "name")
        self.elementClick("submitButton", "id")
