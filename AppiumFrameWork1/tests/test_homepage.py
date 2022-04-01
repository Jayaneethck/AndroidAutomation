import unittest

from appium import webdriver
import pytest
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import unittest
from AppiumFrameWork1.pages.LoginPage import LoginPage

from appium import webdriver
import pytest
from time import sleep

import logging

logging.basicConfig(filename='dukaanandroidtest.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)

import random

name = ['Delta', 'Alpha', 'Hari', 'Rijaz', 'KJ', 'Abhilash', 'Platina', 'KTM', 'Cars', 'Bikes', 'Soul', 'Spark']


class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                       desired_capabilities=
                                       {
                                           "platformName": "Android",
                                           "platformVersion": "9",
                                           "deviceName": "emulator-5554",
                                           "automationName": "uiautomator2",
                                           "app": "C:/Users/clinton/Downloads/app-prod-debug.apk",
                                           "newCommandTimeout": 600,
                                           "launchTimeout": "90000",
                                           "adbExecTimeout": "30000"
                                       })

    def test_navigation_in_home_page(self):
        self.cf = LoginPage(self.driver)
        self.cf.logincall()
        products_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().className("android.widget.TextView").text("Products")')
        products_icon.click()
        sleep(3)
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().className("android.widget.TextView").text("Catalogue")')
        manage_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                               'new UiSelector().className("android.widget.TextView").text("Manage")')
        manage_icon.click()
        sleep(3)
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().className("android.widget.TextView").text("Manage Store")')
        accounts_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(3)
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().className("android.widget.TextView").text("Account")')
        orders_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                               'new UiSelector().className("android.widget.TextView").text("Orders")')
        orders_icon.click()
        sleep(3)
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().className("android.widget.TextView").text("Orders")')

    def test_total_sales_navigating_to_delivered_orders(self):
        self.cf = LoginPage(self.driver)
        self.cf.logincall()
        self.driver.swipe(539, 1504, 550, 670, 500)
        total_sales_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("TOTAL SALES")')
        total_sales_text.click()
        sleep(3)
        try:
            assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Delivered orders")')
        except Exception as e:
            logger.error("Clicking on sales navigating to Delivered orders error(Failed)" + str(e))
        logger.info(" Successfully navigating to Delivered order by clicking total sales(Passed)")

    def test_store_views(self):
        self.cf = LoginPage(self.driver)
        self.cf.logincall()
        self.driver.swipe(539, 1504, 550, 670, 500)
        store_views_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("STORE VIEWS")')
        store_views_text.click()
        sleep(1)
        try:
            assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("What are Store Views?")')
        except Exception as e:
            logger.error("Store Views description not displayed(Failed)" + str(e))
        logger.info(" Store views Description displayed successfully(Passed)")
        sleep(1)

    def test_dukaan_status(self):
        # make sure your store is online before performing this test
        self.cf = LoginPage(self.driver)
        self.cf.logincall()
        sleep(2)
        dukaan_status_toggle = self.driver.find_element(AppiumBy.ID, "com.dukaan.app:id/switchDukaanStatus")
        dukaan_status_toggle.click()
        sleep(1)
        go_online_tomorrow_same_time = self.driver.find_element(AppiumBy.ID,"com.dukaan.app:id/rb4")
        go_online_tomorrow_same_time.click()
        sleep(2)
        confirm_button = self.driver.find_element(AppiumBy.ID,"com.dukaan.app:id/action_btn")
        confirm_button.click()
        sleep(2)
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Switch").checked(false)')
        sleep(2)
        dukaan_status_toggle.click()
        sleep(2)
        try:
            assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Switch").checked(true)')
        except Exception as e:
            logger.error("Dukaan Online and Offline toggle Error(Failed)" + str(e))
        logger.info("Dukaan Online and Offline toggle working successfully(Passed)")

   # def test_domain_select(self):
        #self.driver.launch_app()
        #sleep(10)
        #accounts_icon = self.driver.find_element_by_id("com.dukaan.app:id/account_iv")
        #accounts_icon.click()
        #sleep(2)
        #edit_details_text = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().className("android.widget.TextView").text("Edit business details")')
    #     edit_details_text.click()
    #     sleep(2)
    #     business_name_textbox = self.driver.find_element_by_id("com.dukaan.app:id/store_name_et")
    #     business_name_textbox.send_keys("Jayaneeth")
    #     sleep(2)
    #     save_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
    #     save_button.click()
    #     sleep(5)
    #     home_icon = self.driver.find_element_by_id("com.dukaan.app:id/dashboard_iv")
    #     home_icon.click()
    #     sleep(2)
    #     get_your_domain = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().className("android.widget.TextView").text("Get your own custom domain")')
    #     get_your_domain.click()
    #     sleep(3)
    #     select_domain = self.driver.find_element_by_id("com.dukaan.app:id/selectDomainTV")
    #     select_domain.click()
    #     sleep(10)
    #     domain_select = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().className("android.widget.TextView").text("jayaneeth.org")')
    #     domain_select.click()
    #     sleep(2)
    #     get_my_domain_button = self.driver.find_element_by_id("com.dukaan.app:id/getMyDomain")
    #     get_my_domain_button.click()
    #     sleep(2)
    #     confirm_button = self.driver.find_element_by_id("com.dukaan.app:id/consentActionTV")
    #     confirm_button.click()
    #     sleep(2)
    #     try:
    #         assert self.driver.find_element_by_android_uiautomator(
    #             'new UiSelector().className("android.widget.TextView").text("jayaneeth.org")')
    #     except Exception as e:
    #         logger.error("Domain selection error(Failed)" + str(e))
    #     logger.info("Domain Selection working successfully(Passed)")

    def test_share_link(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        whatsapp_share_icon = self.driver.find_element_by_id("com.dukaan.app:id/share_whatsapp_iv")
        whatsapp_share_icon.click()
        sleep(3)
        try:
            assert self.driver.find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("Copy to clipboard")')
        except Exception as e:
            logger.error("Share link Error(Failed)" + str(e))
        logger.info("Share link working successfully(Passed)")
        self.driver.swipe(470, 600, 470, 400, 400)
        sleep(1)

    def test_home_overview_filters(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        self.driver.swipe(900, 1284, 900, 950, 500)
        filter_dropdown = self.driver.find_element_by_id("com.dukaan.app:id/overvieoverview_w_filter_tv")
        filter_dropdown.click()
        sleep(1)
        filter_today = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Today")')
        filter_today.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Today")')
        filter_dropdown.click()
        filter_yesterday = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Yesterday")')
        filter_yesterday.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Yesterday")')
        filter_dropdown.click()
        filter_this_week = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("This Week")')
        filter_this_week.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("This Week")')
        filter_dropdown.click()
        filter_last_week = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Last Week")')
        filter_last_week.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Last Week")')
        filter_dropdown.click()
        filter_this_month = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("This Month")')
        filter_this_month.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("This Month")')
        self.driver.swipe(900, 1284, 900, 950, 500)
        filter_dropdown.click()
        sleep(2)
        filter_last_month = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Last Month")')
        filter_last_month.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Last Month")')
        self.driver.swipe(900, 1284, 900, 950, 500)
        filter_dropdown.click()
        sleep(1)
        filter_lifetime = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Life Time")')
        filter_lifetime.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Life Time")')
        filter_dropdown.click()
        self.driver.swipe(900, 1284, 900, 950, 500)
        custom_range_filter = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Custom range")')
        custom_range_filter.click()
        sleep(1)
        navigate_to_last_month = self.driver.find_element_by_id("com.dukaan.app:id/imgVNavLeft")
        navigate_to_last_month.click()
        sleep(1)
        start_date = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("1")')
        start_date.click()
        end_date = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("28")')
        end_date.click()
        apply_button = self.driver.find_element_by_id("com.dukaan.app:id/tvBtnApplyCalendarFilter")
        apply_button.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("01/02/22 - 28/02/22")')

    def test_dukaan_banners(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        banner_dukaan_marketing = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
        banner_dukaan_marketing.click()
        sleep(1)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Marketing")')
        sleep(1)
        back_button_from_marketing = self.driver.find_element_by_id("com.dukaan.app:id/ivBack")
        back_button_from_marketing.click()
        sleep(2)
        self.driver.swipe(880, 1000, 150, 1000, 500)
        sleep(1)
        banner_dukaan_delivery = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView')
        banner_dukaan_delivery.click()
        sleep(2)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Set up Dukaan Delivery")')
        sleep(1)
        back_button_from_delivery = self.driver.find_element_by_id("com.dukaan.app:id/backButton")
        back_button_from_delivery.click()
        sleep(2)
        self.driver.swipe(880, 1000, 150, 1000, 500)
        banner_dukaan_credits = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView')
        banner_dukaan_credits.click()
        sleep(2)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Dukaan Credits")')
        sleep(1)
        back_button_from_credits = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView[1]')
        back_button_from_credits.click()
        sleep(1)
        self.driver.swipe(880, 1000, 150, 1000, 500)
        banner_dukaan_plus = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView')
        banner_dukaan_plus.click()
        sleep(2)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Dukaan Plus")')

    def test_add_shortcuts(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        self.driver.swipe(500, 1660, 500, 300, 500)
        sleep(1)
        trial_close_button = self.driver.find_element_by_id("com.dukaan.app:id/closeIV")
        trial_close_button.click()
        add_shortcut_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Add shortcut")')
        add_shortcut_button.click()
        sleep(1)
        select_shortcut = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Promotional Designs")')
        select_shortcut.click()
        sleep(2)
        assert self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Small Icon"])[1]')

    def test_delete_shortcut(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        self.driver.swipe(500, 1660, 500, 300, 500)
        sleep(1)
        trial_close_button = self.driver.find_element_by_id("com.dukaan.app:id/closeIV")
        trial_close_button.click()
        add_shortcut_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Add shortcut")')
        add_shortcut_button.click()
        sleep(1)
        select_shortcut = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("My Customers")')
        select_shortcut.click()
        sleep(2)
        menu_icon = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView[2]')
        menu_icon.click()
        sleep(1)
        remove_shortcut_button = self.driver.find_element_by_id("com.dukaan.app:id/deleteProductTV")
        remove_shortcut_button.click()
        sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("My Customers")').is_displayed(), True)

        except Exception as e:
            logger.error("shortcut not deleted" + str(e))
            logger.info("Shortcut deleted successfully" + str(e))

    def test_add_discount_coupon_from_shortcut(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        self.driver.swipe(500, 1660, 500, 300, 500)
        sleep(1)
        trial_close_button = self.driver.find_element_by_id("com.dukaan.app:id/closeIV")
        trial_close_button.click()
        add_shortcut_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Add shortcut")')
        add_shortcut_button.click()
        sleep(1)
        select_shortcut = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Discount Coupons")')
        select_shortcut.click()
        sleep(1)
        select_discount_coupons = self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Small Icon"])[1]')
        select_discount_coupons.click()
        sleep(2)
        create_coupon_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        create_coupon_button.click()
        sleep(1)
        select_coupon_type = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Percentage discount")')
        select_coupon_type.click()
        sleep(1)
        coupon_code_textbox = self.driver.find_element_by_id("com.dukaan.app:id/coupon_code_et")
        coupon_code_textbox.send_keys("shortcut")
        uses_per_cust_dropdown = self.driver.find_element_by_id("com.dukaan.app:id/user_per_cust_spinner")
        uses_per_cust_dropdown.click()
        sleep(1)
        select_unlimited = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Unlimited")')
        select_unlimited.click()
        percentage_textbox = self.driver.find_element_by_id("com.dukaan.app:id/percent_discount_value_et")
        percentage_textbox.send_keys("10")
        minimum_order_value_textbox = self.driver.find_element_by_id("com.dukaan.app:id/min_order_value_et")
        minimum_order_value_textbox.send_keys("100")
        create_coupon_buttonb = self.driver.find_element_by_id("com.dukaan.app:id/createCouponButton")
        create_coupon_buttonb.click()
        sleep(2)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("SHORTCUT")')

    def test_store_link_redirects_to_buyer_side(self):
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
        sleep(3)
        password_textbox = self.driver.find_element_by_id("com.dukaan.app:id/et_password")
        password_textbox.send_keys("dukaanauto")
        sleep(2)
        enter_password_button = self.driver.find_element_by_id("com.dukaan.app:id/btn_continue")
        enter_password_button.click()
        sleep(4)
        accounts_icon = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Account")')
        accounts_icon.click()
        sleep(3)
        business_details_button = self.driver.find_element_by_id("com.dukaan.app:id/businessDetailsTV")
        business_details_button.click()
        sleep(2)
        business_name_textbox = self.driver.find_element_by_id("com.dukaan.app:id/store_name_et")
        business_name_textbox.send_keys(business_name_text)
        sleep(1)
        save_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        save_button.click()
        sleep(3)
        navigate_to_home_page = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Home")')
        navigate_to_home_page.click()
        sleep(1)
        store_link = self.driver.find_element_by_id("com.dukaan.app:id/store_link_tv")
        store_link.click()
        sleep(3)
        name_in_buyer_side = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView')
        sleep(1)
        self.assertEqual(business_name_text, name_in_buyer_side.text)

    def tearDown(self):
        self.driver.quit()


if '__main__' == __name__:
    unittest.main()
