import time

import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


def get_data():
    return [

        ["Delhi"],
        ["Dubai"],
        ["America"]


    ]


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['udid'] = 'emulator-5554'
    #desired_caps['appPackage'] = 'com.goibibo'
    #desired_caps['appActivity'] = 'com.goibibo.hotel.autosuggest.uiControllers.AutosuggestActivity'
    #"app": "C:/Users/clinton/Downloads/app-prod-debug.apk"
    desired_caps['app'] = 'C:/Users/clinton/Downloads/goibibo-14-4-3.apk'
    desired_caps['noReset'] = True
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)


def teardown_function():
    time.sleep(2)
    driver.quit()
    appium_service.stop()


@pytest.mark.parametrize("city", get_data())
def test_dologin(city):
   print(city)