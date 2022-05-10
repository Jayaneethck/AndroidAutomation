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

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from AppiumFrameWork1.pages.LoginPage import LoginPage

def test_login_with_email(appium_driver):
        driver = appium_driver
        cf = LoginPage(driver)
        cf.logincall()
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Home")')))

def test_login_with_mobile(appium_driver):
        driver =  appium_driver
        get_started_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/get_started")))
        get_started_button.click()
        '''mobile_number_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_mobile_no")
        mobile_number_textbox.send_keys("1111111112")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        otp_textbox = self.driver.find_element_by_id("1d13d877-636d-4ec0-9663-7ce3512c4b87")
        # otp_textbox = self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.TextView").text(" ")')
        otp_textbox.send_keys("723573")'''
        #autofill_mobile = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/text1")))
        #autofill_mobile.click()
        mobile_number_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("Mobile Number")')))
        mobile_number_textbox.send_keys("")
        mobile_number_textbox.send_keys("1111111112")
        continue_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Continue")')))
        continue_button.click()
        #send_otp_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Send OTP")')))
        #send_otp_button.click()
        otp_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "1d13d877-636d-4ec0-9663-7ce3512c4b87")))
        otp_textbox.send_keys("723573")
        #otp_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')))
        #otp_textbox.send_keys("723573")
        assert driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Home")')

