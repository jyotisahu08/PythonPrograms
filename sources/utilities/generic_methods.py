import logging
import os
import time
from traceback import print_stack
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sources.utilities.custom_logger as cl


class GenericMethods():
    logMsg = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time()) * 1000) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.logMsg.info("Screenshot saved to directory:" + destinationFile)
        except:
            self.logMsg.error("#### Exception occurred")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partiallink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.logMsg.info("Locator type" + locatorType + " not correct/supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.logMsg.info("Element found with locator: " + locator + "and locator type:" + locatorType)
        except:
            self.logMsg.info("Element not found with locator: " + locator + "and locator type:" + locatorType)
        return element

    def clearText(self, locator, locatorType="id"):
        try:
            self.getElement(locator, locatorType).clear()
            self.logMsg("The text field is cleared with locator" + locator + " and locator type " + locatorType)
        except:
            self.logMsg.error("#### Not able to clear ####")
            print_stack()

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.logMsg.info("Clicked on element with locator " + locator + "locatorType: " + locatorType)
        except:
            self.logMsg.info("cannot click on the element with locator: " + locator + "locatorType: " + locatorType)

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.logMsg.info("Sent data on element with locator: " + locator + " locator type: " + locatorType)
        except:
            self.logMsg.info("Cannot Send data on element with locator: " + locator + " locator type: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.logMsg.info("Element found")
                return True
            else:
                self.logMsg.info("Element not found")
                return False
        except:
            self.logMsg.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.logMsg.info("Element Found")
                return True
            else:
                self.logMsg.info("Element not Found")
                return False
        except:
            self.logMsg.info("Element not Found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.logMsg.info("Waiting for maximum :: " + str(timeout) +
                             ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(byType, locator))
            self.logMsg.info("Element appeared on the web page")
        except:
            self.logMsg.info("Element not appeared on the web page")
            print_stack()
        return element

    def switch_to_child_window(self,driver):
        child_window = None
        parent_window = driver.current_window_handle
        window_ids = driver.window_handles
        try:
            for window_id in window_ids:
                if window_id != parent_window:
                    child_window = window_id
                    break
            driver.switch_to.window(child_window)
            self.logMsg.info("Switched to the child window")
        except Exception:
            self.logMsg.info("Unable to switch to the child window")
            # print_stack()

    def timeSleep(self,timeInSec):
        time.sleep(timeInSec)

    def getText(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            text_element = element.text
            self.logMsg.info("VisibleText of web Element is captured")
        except Exception:
            self.logMsg.info("VisibleText of web Element is not captured")
        return text_element







