import unittest

from appium import webdriver
import pytest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

from appium import webdriver
import pytest
from time import sleep


class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                       desired_capabilities=
                                       {
                                           "platformName": "Android",
                                           "platformVersion": "9",
                                           "deviceName": "92d5ac50",
                                           "automationName": "uiautomator2",
                                           "app": "C:/Users/clinton/Downloads/app-prod-debug.apk",
                                           "newCommandTimeout": 600,
                                           "launchTimeout": "90000",
                                           "adbExecTimeout": "30000"
                                       })

    def test_login_with_email(self):
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        continue_with_email_button = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Continue with Email")')
        continue_with_email_button.click()
        sleep(1)
        email_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_input")
        email_address_textbox.send_keys("clintonvinoth97@gmail.com")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("Clinton@97")
        sleep(1)
        show_password = self.driver.find_element_by_id("com.dukaan.app:id/tv_hide_show")
        show_password.click()
        sleep(1)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        assert self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Home")')

    def test_login_with_mobile(self):
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        mobile_number_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_mobile_no")
        mobile_number_textbox.send_keys("1111111112")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        otp_textbox = self.driver.find_element_by_id("1d13d877-636d-4ec0-9663-7ce3512c4b87")
        # otp_textbox = self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.TextView").text(" ")')
        otp_textbox.send_keys("723573")
        sleep(5)
        assert self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Home")')

    def tearDown(self):
        self.driver.quit()

    if '__main__' == __name__:
        unittest.main()
