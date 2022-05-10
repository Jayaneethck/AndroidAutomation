import unittest
from lib2to3.pgen2 import driver

from appium import webdriver
from AppiumFrameWork1.pages.LoginPage import LoginPage


class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = "92d5ac50"
        desired_caps["automationName"] = "uiAutomator1"
        desired_caps["app"] = ('C:/Users/clinton/Downloads/app-prod-debug.apk')
        desired_caps["newCommandTimeout"] = "600"
        desired_caps["launchTimeout"] = "90000"
        desired_caps["adbExecTimeout"] = "30000"
        desired_caps["autoGrantPermissions"] = "true"
        driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)
        return driver

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
        driver1 = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)
        return driver1
