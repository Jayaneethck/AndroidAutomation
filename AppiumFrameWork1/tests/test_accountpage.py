import unittest

from appium import webdriver
import pytest
from time import sleep

import unittest

from appium import webdriver
import pytest
from time import sleep

import random

name = ['Rahul', 'Arjun', 'Ravi', 'Hari', 'Nikhil', 'Sachin', 'Suresh', 'Manu', 'Rishi', 'Varun', 'Prithwi', 'Ajil']


class AccountPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                       desired_capabilities=
                                       {
                                           "platformName": "Android",
                                           "platformVersion": "9",
                                           "deviceName": "92d5ac50",
                                           "automationName": "uiautomator2",
                                           "app": "/Users/jayaneethck/Desktop/App/app-prod-debug.apk",
                                           "newCommandTimeout": 600,
                                           "launchTimeout": "90000",
                                           "adbExecTimeout": "30000",
                                           "autoGrantPermissions": "true"
                                       })

    def test_edit_business_name(self):
        business_name_text = random.choice(name)
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        continue_with_email_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
        continue_with_email_button.click()
        sleep(1)
        email_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_input")
        email_address_textbox.send_keys("jayaneethck@gmail.com")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(1)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        accounts_icon = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(1)
        edit_details_text = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Edit business details")')
        edit_details_text.click()
        sleep(1)
        business_name_textbox = self.driver.find_element_by_id("com.dukaan.app:id/store_name_et")
        business_name_textbox.send_keys(business_name_text)
        sleep(1)
        save_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        save_button.click()
        sleep(2)
        self.assertEqual(self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Store details updated")').is_displayed(), True)



    def test_update_store_logo(self):
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        continue_with_email_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
        continue_with_email_button.click()
        sleep(1)
        email_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_input")
        email_address_textbox.send_keys("jayaneethck@gmail.com")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(3)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(3)
        accounts_icon = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(1)
        edit_business_details_button = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Edit business details")')
        edit_business_details_button.click()
        sleep(2)
        update_logo_button = self.driver.find_element_by_id("com.dukaan.app:id/tvSelectImage")
        update_logo_button.click()
        sleep(1)
        gallery_icon = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Gallery")')
        gallery_icon.click()
        sleep(1)
        folder_select = self.driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='Folder'])[1]")
        folder_select.click()
        sleep(1)
        image_select = self.driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='Image'])[2]")
        image_select.click()
        sleep(3)
        save_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        save_button.click()
        sleep(2)
        assert self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Store details updated")')

    def test_delete_store_logo(self):
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        continue_with_email_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
        continue_with_email_button.click()
        sleep(1)
        email_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_input")
        email_address_textbox.send_keys("jayaneethck@gmail.com")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(3)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        accounts_icon = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(2)
        edit_business_details_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Edit business details")')
        edit_business_details_button.click()
        sleep(2)
        update_logo_button = self.driver.find_element_by_id("com.dukaan.app:id/tvSelectImage")
        update_logo_button.click()
        sleep(2)
        gallery_icon = self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Small Icon"])[2]')
        gallery_icon.click()
        sleep(3)
        folder_select = self.driver.find_element_by_id("com.dukaan.app:id/image")
        folder_select.click()
        sleep(2)
        image_select = self.driver.find_element_by_id("com.dukaan.app:id/image_view")
        image_select.click()
        sleep(6)
        save_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        save_button.click()
        sleep(4)
        edit_business_details_button.click()
        sleep(4)
        remove_image_button = self.driver.find_element_by_id("com.dukaan.app:id/remove_image_iv")
        remove_image_button.click()
        sleep(1)
        save_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        save_button.click()
        sleep(5)
        edit_business_details_button.click()
        sleep(4)
        assert self.driver.find_element_by_id("com.dukaan.app:id/store_image_pick_rl")

    def test_add_new_business_category(self):
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        continue_with_email_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
        continue_with_email_button.click()
        sleep(1)
        email_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_input")
        email_address_textbox.send_keys("jayaneethck@gmail.com")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(3)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        accounts_icon = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(2)
        edit_business_details_button = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Edit business details")')
        edit_business_details_button.click()
        sleep(1)
        business_category = self.driver.find_element_by_id("com.dukaan.app:id/store_category_et")
        business_category.click()
        sleep(1)
        self.driver.swipe(470, 760, 470, 66, 400)
        sleep(1)
        self.driver.swipe(470, 1750, 470, 100, 400)
        business_category_not_listed = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("My business category is not listed")')
        business_category_not_listed.click()
        sleep(1)
        business_category_textbox = self.driver.find_element_by_id("com.dukaan.app:id/category_name_et")
        business_category_textbox.send_keys("Healthcare")
        sleep(1)
        save_button = self.driver.find_element_by_id("com.dukaan.app:id/new_category_save_tv")
        save_button.click()
        sleep(2)
        save_business_details_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        save_business_details_button.click()
        sleep(3)
        edit_business_details_button.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.EditText").text("Healthcare")')

    def test_logout(self):
        self.driver.launch_app()
        sleep(2)
        get_started_button = self.driver.find_element_by_id("com.dukaan.app:id/get_started")
        get_started_button.click()
        sleep(1)
        continue_with_email_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
        continue_with_email_button.click()
        sleep(1)
        email_address_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_input")
        email_address_textbox.send_keys("jayaneethck@gmail.com")
        sleep(1)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        continue_button.click()
        sleep(2)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(3)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        accounts_icon = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(1)
        self.driver.swipe(542, 1666, 542, 1000, 400)
        sleep(1)
        additional_info = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Additional Information")')
        additional_info.click()
        sleep(1)
        signout_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Sign Out")')
        signout_button.click()
        sleep(1)
        signout_confirm = self.driver.find_element_by_id("com.dukaan.app:id/tv_yes")
        signout_confirm.click()
        sleep(2)
        assert self.driver.find_element_by_id("com.dukaan.app:id/get_started")

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




    def tearDown(self):
        self.driver.quit()


if '__main__' == __name__:
    unittest.main()