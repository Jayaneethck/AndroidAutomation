
from appium.webdriver import webdriver


from appium import webdriver
import pytest


@pytest.fixture(params=["device1"], scope="function")
def appium_driver(request):
    global driver
    if request.param == "device1":
        desired_caps = {}
        desired_caps["platformName"] = 'Android'
        desired_caps["platformVersion"] = '9'
        desired_caps["deviceName"] = 'Android'
        desired_caps["udid"] = '92d5ac50'
        desired_caps["automationName"] = 'uiAutomator1'
        desired_caps["app"] = ('C:/Users/clinton/Downloads/app-prod-debug.apk')
        desired_caps["newCommandTimeout"] = '600'
        desired_caps["launchTimeout"] = '90000'
        desired_caps["adbExecTimeout"] = '30000'
        desired_caps["autoGrantPermissions"] = 'true'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)







    driver.implicitly_wait(15)
    yield driver
    driver.quit()

