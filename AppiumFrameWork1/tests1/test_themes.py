import unittest
import json
import time
# import pytest
import unittest
from lib2to3.pgen2 import driver

import substring

from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import url
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import datetime
import os
import pytz

import random
from selenium.webdriver.chrome.options import Options

import self
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import unittest
from appium import webdriver
import pytest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import pytest

import random

from selenium.webdriver.support.wait import WebDriverWait

from AppiumFrameWork1.tests.test_homepage import logger
from AppiumFrameWork1.pages.LoginPage import LoginPage

name = ['Delta', 'Alpha', 'Hari', 'Rijaz', 'KJ', 'Abhilash', 'Platina', 'KTM', 'Cars', 'Bikes', 'Soul', 'Spark']


class HomePage(unittest.TestCase):

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

    def test_address_buyer_side(self):
        '''enter_name = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText")))
        enter_name.send_keys("vinoth")
        mobile_number = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.EditText")))
        mobile_number.send_keys("8838569124")
        sleep(2)
        self.driver.swipe(575, 1096, 524, 900, 400)
        sleep(3)
        enter_address = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.widget.EditText")))
        enter_address.click()
        enter_address.send_keys("23 Hsr Layout 5th sector")
        sleep(5)
        self.driver.swipe(537, 998, 556, 450, 400)
        sleep(5)
        sleep(3)
        self.driver.swipe(493,1601,531,950,400)
        sleep(3)
        #enter_pincode = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.widget.EditText")))
        #enter_pincode.send_keys("560105")
        enter_city = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View[2]/android.widget.EditText")))
        enter_city.send_keys("Bangalore")
        sleep(5)
        self.driver.swipe(496, 1131, 556, 370, 400)
        sleep(5)
        state_dropdown = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[6]/android.view.View[2]/android.view.View/android.view.View[2]")))
        state_dropdown.click()
        click_on_state = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").text("Gujarat")')))
        click_on_state.click()'''

    def test_leo_theme_redirect_to_buyer_side_place_order(self):
        self.cf = LoginPage(self.driver)
        self.cf.logincall()
        manage_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        dukaan_theme = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]/android.widget.FrameLayout/android.widget.LinearLayout")))
        dukaan_theme.click()
        time.sleep(3)
        self.driver.swipe(565, 1402, 553, 700, 400)
        time.sleep(3)
        active_leo_theme = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Apply")')))
        active_leo_theme.click()
        home_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Home")')))
        home_icon.click()
        home_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Home")')))
        home_icon.click()
        click_url = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("mydukaan.io/dukaan6986")')))
        click_url.click()
        time.sleep(3)
        self.driver.swipe(565, 1402, 553, 600, 400)
        time.sleep(3)
        click_on_asus_laptop_product = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Asus Laptop")')))
        click_on_asus_laptop_product.click()
        add_to_bag = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Add to bag")')))
        add_to_bag.click()
        time.sleep(3)
        self.driver.swipe(556, 1724, 578, 550, 400)
        time.sleep(3)
        add_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("ADD")')))
        add_button.click()
        click_on_bag_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("2")')))
        click_on_bag_icon.click()
        time.sleep(3)
        self.driver.swipe(508, 1437, 534, 600, 400)
        time.sleep(3)
        click_popular_product = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Dell")')))
        click_popular_product.click()
        add_to_bag = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Add to bag")')))
        add_to_bag.click()
        go_to_bag = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Go to bag")')))
        go_to_bag.click()
        click_on_continue = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Continue")')))
        click_on_continue.click()
        click_loginhere = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").text("Already a user? Log in here")')))
        click_loginhere.click()
        autofill_mobile = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/text1")))
        autofill_mobile.click()
        mobile_number_textbox = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText')))
        mobile_number_textbox.send_keys("")
        mobile_number_textbox.send_keys("1111111112")
        send_otp_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Send OTP")')))
        send_otp_button.click()
        otp_textbox = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')))
        otp_textbox.send_keys("723573")
        continue_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Continue")')))
        continue_button.click()
        sleep(3)
        self.driver.swipe(540, 1749, 575, 1004, 400)
        sleep(3)
        continue_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Continue")')))
        continue_button.click()
        place_order = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").text("Place order")')))
        place_order.click()
        assert WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Your order is successful!")')))


    def test_business_category_for_2themes(self):
        self.cf = LoginPage(self.driver)
        self.cf.logincall()
        account_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        account_icon.click()
        edit_business_details = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Edit business details")')))
        edit_business_details.click()
        business_category = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/store_category_et")))
        business_category.click()
        click_mob_computer_other_accesories = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Mobile, Computers & Other Accessories")')))
        click_mob_computer_other_accesories.click()
        save_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Save")')))
        save_button.click()
        manage_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        dukaan_theme = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]/android.widget.FrameLayout/android.widget.LinearLayout")))
        dukaan_theme.click()
        assert WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Themes")')))




    def tearDown(self):
        self.driver.quit()


if '__main__' == __name__:
    unittest.main()
