import unittest

from appium import webdriver
import pytest
from time import sleep
import torch

import unittest
from appium import webdriver
import pytest
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from AppiumFrameWork1.pages.LoginPage import LoginPage
from AppiumFrameWork1.tests1.conftest import appium_driver
from AppiumFrameWork1.pages.DriverClass import Driver
import random

name = ['Rahul', 'Arjun', 'Ravi', 'Hari', 'Nikhil', 'Sachin', 'Suresh', 'Manu', 'Rishi', 'Varun', 'Prithwi', 'Ajil']



#class AccountPage(unittest.TestCase):



def test_edit_business_name(appium_driver):
        driver = appium_driver
        business_name_text = random.choice(name)
        cf = LoginPage(driver)
        cf.logincall()
        accounts_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        accounts_icon.click()
        edit_details_text = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Edit business details")')))
        edit_details_text.click()
        business_name_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/store_name_et")))
        business_name_textbox.send_keys(business_name_text)
        save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/email_et")))
        save_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Store details updated")')))

def test_update_store_logo(appium_driver):
        driver = appium_driver
        cf = LoginPage(driver)
        cf.logincall()
        accounts_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        accounts_icon.click()
        edit_details_text = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Edit business details")')))
        edit_details_text.click()
        update_logo_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/tvSelectImage")))
        update_logo_button.click()
        gallery_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Gallery")')))
        gallery_icon.click()
        folder_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "	//android.widget.ImageView[@content-desc='Folder']")))
        folder_select.click()
        image_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/image_view")))
        image_select.click()
        save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Save")')))
        save_button.click()
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Store details updated")')))

def test_delete_store_logo(appium_driver):
        driver = appium_driver
        cf = LoginPage(driver)
        cf.logincall()
        accounts_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        accounts_icon.click()
        edit_details_text = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Edit business details")')))
        edit_details_text.click()
        update_logo_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/tvSelectImage")))
        update_logo_button.click()
        gallery_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[2]')))
        gallery_icon.click()
        folder_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/image")))
        folder_select.click()
        image_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/image_view")))
        image_select.click()
        save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        save_button.click()
        edit_details_text.click()
        remove_image_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/remove_image_iv")))
        remove_image_button.click()
        save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Save")')))
        save_button.click()
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Store details updated")')))


def test_add_new_business_category(appium_driver):
        driver = appium_driver
        cf = LoginPage(driver)
        cf.logincall()
        accounts_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        accounts_icon.click()
        edit_business_details_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Edit business details")')))
        edit_business_details_button.click()
        business_category = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/store_category_et")))
        business_category.click()
        driver.swipe(470, 760, 470, 66, 400)
        sleep(3)
        driver.swipe(470, 1750, 470, 100, 400)
        sleep(3)
        business_category_not_listed = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("My business category is not listed")')))
        business_category_not_listed.click()
        business_category_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/category_name_et")))
        business_category_textbox.send_keys("Healthcare")
        save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/new_category_save_tv")))
        save_button.click()
        save_business_details_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        save_business_details_button.click()
        edit_business_details_button.click()
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("Healthcare")')))

def test_logout(appium_driver):
        driver = appium_driver
        cf = LoginPage(driver)
        cf.logincall()
        accounts_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        accounts_icon.click()
        sleep(3)
        driver.swipe(542, 1666, 542, 1000, 400)
        sleep(3)
        additional_info = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Additional Information")')))
        additional_info.click()
        signout_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Sign Out")')))
        signout_button.click()
        signout_confirm = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/tv_yes")))
        signout_confirm.click()
        sleep(2)
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/get_started")))

        # def test_edit_business_address(self):
        #     self.driver.launch_app()
        #     sleep(10)
        #     accounts_icon = self.driver.find_element_by_id("com.dukaan.app:id/account_iv")
        #     accounts_icon.click()
        #     sleep(1)
        #     edit_business_details_button = self.driver.find_element_by_android_uiautomator(
        #         'new UiSelector().className("android.widget.TextView").text("Edit business details")')
        #     edit_business_details_button.click()
        #     sleep(3)
        #     store_address = self.driver.find_element_by_id("com.dukaan.app:id/store_address_et")
        #     store_address.click()
        #     sleep(4)
        #     change_address = self.driver.find_element_by_id("com.dukaan.app:id/change_address_tv")
        #     change_address.click()
        #     sleep(2)
        #     search_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/address_et")
        #     search_address_textbox.send_keys("dukaan kal")
        #     sleep(5)
        #     location = self.driver.find_element_by_id("com.dukaan.app:id/name_tv")
        #     location.click()
        #     sleep(1)
        #     location.click()
        #     sleep(4)
        #     save_address_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        #     save_address_button.click()
        #     sleep(4)
        #     assert self.driver.find_element_by_android_uiautomator(
        #         'new UiSelector().className("android.widget.EditText").text("131/1, Dukaan Kalwar Rd, Chandra Nagar, Gokulpura, Jaipur, Rajasthan 302012, India")')

