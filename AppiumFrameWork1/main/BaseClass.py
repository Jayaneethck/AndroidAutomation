from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.CustomLogger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element

        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element

        elif locatorType == "des":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          'UiSelector().description("%s")' % (locatorValue)))
            return element

        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index("%d")' % int(locatorValue)))
            return element

        elif locatorType == "text":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorValue))
            return element

        elif locatorType == "xpath":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.XPATH, '%s' % locatorValue))
            return element
        else:
            self.log.info("locator value" + locatorValue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType:" + locatorType + "with the locator value :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType:" + locatorType + "with the locator value :" + locatorValue)

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Click on Element found with LocatorType:" + locatorType + "with the locator value :" + locatorValue)
        except:
            self.log.info("Unable to Click on Element not found with LocatorType:"
                          + locatorType + "with the locator value :" + locatorValue)

    def sendText(self, text, locatorValue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Click on Element found with LocatorType:" + locatorType + "with the locator value :" + locatorValue)
        except:
            self.log.info(
                "Unable to Click on Element not found with LocatorType:" + locatorType + "with the locator value :" + locatorValue)

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Element with LocatorType:" + locatorType + "with the locator value :" + locatorValue + "is displayed")
            return True
        except:
            self.log.info(
                "Element with LocatorType:" + locatorType + "with the locator value :" + locatorValue + "is not displayed")
            return False

    def screenShot(self, screenShotName):
        filename = screenShotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/screenshotss"
        screenshotPath = screenshotDirectory + filename
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("screenshot save to path:" + screenshotPath)
        except:
            self.log.info("unable to save screenshot to the path :" + screenshotPath)

    def keyCodes(self, value):
        self.driver.press_keycode(value)

    #def asserts(self, text):
        #self.driver.is_displayed(text)

