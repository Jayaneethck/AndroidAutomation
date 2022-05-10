from appium.webdriver import webdriver


class Driver1:
    def getDriverMethod1(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = "138276037200179"
        desired_caps["automationName"] = "uiAutomator2"
        desired_caps["app"] = ('C:/Users/clinton/Downloads/app-prod-debug.apk')
        desired_caps["newCommandTimeout"] = "600"
        desired_caps["launchTimeout"] = "90000"
        desired_caps["adbExecTimeout"] = "30000"
        desired_caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)

        return driver