from AppiumFrameWork1.pages.LoginPage import LoginPage
from appium import webdriver as AppiumDriver


def test_login():
    Desired_Capabilities = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'platformVersion': '9',
        'app': 'C:/Users/clinton/Downloads/app-prod-debug.apk',
        'udid': '92d5ac50',
        'deviceName': 'Mi A2',
        'appPackage': 'com.android.settings',
        'appActivity': 'com.android.settings.Settings$MyDeviceInfoActivity',
        'systemPort': 8200

    }
    driver = AppiumDriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=Desired_Capabilities)
    login = LoginPage(driver)
    login.logincall()


