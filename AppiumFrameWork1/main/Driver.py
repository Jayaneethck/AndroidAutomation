from appium.webdriver import webdriver


def setUp(self):
    self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4724/wd/hub",
                                   desired_capabilities=
                                   {
                                       "platformName": "Android",
                                       "platformVersion": "9",
                                       "deviceName": "92d5ac50",
                                       "automationName": "uiautomator2",
                                       "app": "C:/Users/clinton/Downloads/app-prod-debug.apk",
                                       "newCommandTimeout": 600,
                                       "launchTimeout": "90000",
                                       "adbExecTimeout": "30000",
                                       "autoGrantPermissions": "true"
                                   })

    return driver
