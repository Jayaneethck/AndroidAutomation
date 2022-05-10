import unittest

import self
from appium import webdriver
import pytest
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AppiumFrameWork1.pages.Alerting import slackalerts

from AppiumFrameWork1.tests1.conftest import appium_driver

# from slack.errors import SlackApiError


logging.basicConfig(filename='dukaanandroidautomation.log', filemode='w')
logger = logging.getLogger(__name__)
from time import sleep
from AppiumFrameWork1.pages.LoginPage import LoginPage

# driver= self.driver

name = ['Rahul', 'Arjun', 'Ravi', 'Hari', 'Nikhil', 'Sachin', 'Suresh', 'Manu', 'Rishi', 'Varun', 'Prithwi', 'Ajil']


def test_01create_discount_coupon_as_percentage(appium_driver):
    # ensure there is already a coupon added
    try:
        coupon_code = ("PERCOUPON5")
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        select_discount_type = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        select_discount_type.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys(coupon_code)
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
        custom_select.click()
        uses_per_cust_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_cstom_et")))
        uses_per_cust_textbox.send_keys("50")
        percent_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/percent_discount_value_et")))
        percent_textbox.send_keys("20")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/min_order_value_et")))
        min_order_amount.send_keys("300")
        driver.hide_keyboard()
        max_discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/maximum_discount_et")))
        max_discount_amount_textbox.send_keys("100")
        driver.hide_keyboard()
        coupon_validity = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Coupon validity")')))
        coupon_validity.click()
        start_date = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/date_from")))
        start_date.click()
        month_navigation = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/next")))
        month_navigation.click()
        start_date_selection = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").text("1")')))
        start_date_selection.click()
        select_time = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/time_from")))
        select_time.click()
        done_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/timeDone")))
        done_button.click()
        create_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/createCouponButton")))
        create_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("PERCOUPON5")')))

    except:
        print("except")
        slackalerts().slackalert(result="test_create_discount_coupon_as_percentage-failed")


# def test_delete_coupon(appium_driver):
#     try:
#             driver = appium_driver
#             logincall = LoginPage(driver)
#             logincall.logincall()
#             manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
#             manage_icon.click()
#             discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
#             discount_coupons_icon.click()
#             create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
#             create_coupon_button.click()
#             select_discount_type = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
#             select_discount_type.click()
#             coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
#             coupon_code_textbox.send_keys("PERCOUPON4")
#             uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
#             uses_per_cust_dropdown.click()
#             unlimited_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Unlimited")')))
#             unlimited_select.click()
#             percent_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/percent_discount_value_et")))
#             percent_textbox.send_keys("12")
#             min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/min_order_value_et")))
#             min_order_amount.send_keys("3000")
#             driver.hide_keyboard()
#             max_discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/maximum_discount_et")))
#             max_discount_amount_textbox.send_keys("500")
#             driver.hide_keyboard()
#             create_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/createCouponButton")))
#             create_button.click()
#             coupon_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("PERCOUPON4")')))
#             coupon_select.click()
#             sleep(3)
#             driver.swipe(470, 760, 470, 66, 400)
#             sleep(3)
#             delete_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/deleteCouponTV")))
#             delete_coupon.click()
#             confirm_delete = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/consentActionTV")))
#             confirm_delete.click()
#             driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("PERCOUPON4")').is_displayed(), True)
#     except Exception as e:
#             logger.error("Discount coupon not deleted" + str(e))
#             logger.info("Discount coupon deleted successfully" + str(e))
#             slackalerts().slackalert(result="test_delete_coupon-failed")


def test_create_discount_coupon_as_flat_discount(appium_driver):
    # ensure there is already a coupon added
    try:
        coupon_code = ("FLATDISC1")
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        select_discount_type = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
        select_discount_type.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys(coupon_code)
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        only_once_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Only once")')))
        only_once_select.click()
        discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_discount_value_et")))
        discount_amount_textbox.send_keys("50")
        min_order_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_min_order_value_et")))
        min_order_amount_textbox.send_keys("500")
        driver.hide_keyboard()
        create_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/createCouponButton")))
        create_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("FLATDISC1")')))

    except:
        print("except")
        slackalerts().slackalert(result="test_create_discount_coupon_as_flat_discount-failed")


def test_create_discount_coupon_as_buy_x_get_y(appium_driver):
    # ensure there is already a coupon added
    try:
        coupon_code = ("BUYXGETY1")
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        bgxy_discount_type = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Offer FREE products on purchase of certain number of items.")')))
        bgxy_discount_type.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys(coupon_code)
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        unlimited_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Unlimited")')))
        unlimited_select.click()
        buy_x = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextBuy")))
        buy_x.send_keys("2")
        get_y = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextGet")))
        get_y.send_keys("1")
        coupon_apply_on = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/couponOptionTv")))
        coupon_apply_on.click()
        all_products_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("All products")')))
        all_products_select.click()
        create_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/createCouponButton")))
        create_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("BUYXGETY1")')))

    except:
        print("except")
        slackalerts().slackalert(result="test_create_discount_coupon_as_buy_x_get_y-failed")



def test_check_visibility_in_discountcoupon(appium_driver):
   try:
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Discount Coupons")')))
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        search_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/search")))
        search_icon.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("Search")')))
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
        # assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Buy X Get Y Free")')))

   except:
       print("except")
       slackalerts().slackalert(result="test_check_visibility_in_discountcoupon-failed")

def test_create_percentage_discount_with_coupon_code_empty(appium_driver):
    try:
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        percentage_discount_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        percentage_discount_coupon.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("")
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        unlimited_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Unlimited")')))
        unlimited_select.click()
        percent_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/percent_discount_value_et")))
        percent_textbox.send_keys("12")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/min_order_value_et")))
        min_order_amount.send_keys("3000")
        driver.hide_keyboard()
        max_discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/maximum_discount_et")))
        max_discount_amount_textbox.send_keys("500")
        driver.hide_keyboard()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/createCouponButton")))
        create_coupon_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Minimum length is 5 characters")')))
    except:
        print("except")
        slackalerts().slackalert(result="test_create_percentage_discount_with_coupon_code_empty-failed")

def test_create_percentage_discount_with_users_per_customer_as_empty(appium_driver):
    try:
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        percentage_discount_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        percentage_discount_coupon.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("CNUPCE")
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
        custom_select.click()
        percent_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/percent_discount_value_et")))
        percent_textbox.send_keys("12")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/min_order_value_et")))
        min_order_amount.send_keys("3000")
        driver.hide_keyboard()
        # driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)
        # driver.assertEqual(driver.find_element_by_id("com.dukaan.app:id/addUpdateProductButton").is_displayed(), True)
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))
        print("except")
        slackalerts().slackalert(result="test_create_percentage_discount_with_users_per_customer_as_empty-failed")



def test_create_percentage_discount_with_percentage_as_empty(appium_driver):
    try:

        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        percentage_discount_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        percentage_discount_coupon.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("CNUPCE")
        User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
        User_per_customer_button.click()
        # uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        # uses_per_cust_dropdown.click()
        custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
        custom_select.send_keys("400")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/min_order_value_et")))
        min_order_amount.send_keys("3000")
        driver.hide_keyboard()
        # driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)
        # driver.assertEqual(driver.find_element_by_id("com.dukaan.app:id/addUpdateProductButton").is_displayed(), True)
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))
        print("except")
        slackalerts().slackalert(result="test_create_percentage_discount_with_percentage_as_empty-failed")


def test_create_percentage_discount_with_minimum_order_value_as_empty(appium_driver):

    try:

        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        percentage_discount_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        percentage_discount_coupon.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("CNUPCE")
        # User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
        # User_per_customer_button.click()
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
        custom_select.click()
        percent_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/percent_discount_value_et")))
        percent_textbox.send_keys("12")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/min_order_value_et")))
        min_order_amount.send_keys("")
        driver.hide_keyboard()
        # driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)
        # driver.assertEqual(driver.find_element_by_id("com.dukaan.app:id/addUpdateProductButton").is_displayed(), True)
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))
        print("except")
        slackalerts().slackalert(result="test_create_percentage_discount_with_minimum_order_value_as_empty-failed")



def test_switch_in_coupon_types(appium_driver):
    try:

        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        percentage_discount_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        percentage_discount_coupon.click()
        percentage_switch_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        percentage_switch_coupon.click()
        flat_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        flat_coupon_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Create coupon")')))
        flat_switch_coupon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Percentage discount")')))
        flat_switch_coupon.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Create coupon")')))
        bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Buy X Get Y Free")')))
        bxgy_coupon_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Buy X Get Y Free")')))

    except:
        print("except")
        slackalerts().slackalert(result="test_switch_in_coupon_types-failed")


def test_create_flat_discount_with_coupon_code_empty(appium_driver):

    try:

        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        flat_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
        flat_coupon_button.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("")
        uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        uses_per_cust_dropdown.click()
        unlimited_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Unlimited")')))
        unlimited_select.click()
        discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_discount_value_et")))
        discount_amount_textbox.send_keys("12")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_min_order_value_et")))
        min_order_amount.send_keys("12")
        driver.hide_keyboard()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/createCouponButton")))
        create_coupon_button.click()
        assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Minimum length is 5 characters")')))
    except:
        print("except")
        slackalerts().slackalert(result="test_create_flat_discount_with_coupon_code_empty-failed")


def test_create_flat_discount_with_users_per_customer_as_empty(appium_driver):
    try:
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        flat_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
        flat_coupon_button.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("CNUPCE")
        # uses_per_cust_dropdown = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/user_per_cust_spinner")))
        # uses_per_cust_dropdown.click()
        # custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
        # custom_select.click()
        discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_discount_value_et")))
        discount_amount_textbox.send_keys("12")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_min_order_value_et")))
        min_order_amount.send_keys("12")
        driver.hide_keyboard()
        # driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)
        # driver.assertEqual(driver.find_element_by_id("com.dukaan.app:id/addUpdateProductButton").is_displayed(), True)

        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))
        print("except")
        slackalerts().slackalert(result="test_create_flat_discount_with_users_per_customer_as_empty-failed")



def test_create_flat_discount_with_discount_amount_as_empty(appium_driver):
    try:
        driver = appium_driver
        logincall = LoginPage(driver)
        logincall.logincall()
        manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
        manage_icon.click()
        discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
        discount_coupons_icon.click()
        create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
        create_coupon_button.click()
        flat_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
        flat_coupon_button.click()
        coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
        coupon_code_textbox.send_keys("CNUPCE")
        User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
        User_per_customer_button.click()
        custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
        custom_select.click()
        discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_discount_value_et")))
        discount_amount_textbox.send_keys("")
        min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_min_order_value_et")))
        min_order_amount.send_keys("12")
        driver.hide_keyboard()
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))
        print("except")
        slackalerts().slackalert(result="test_create_flat_discount_with_discount_amount_as_empty-failed")


def test_create_flat_discount_with_minimum_order_value_as_empty(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    flat_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
    flat_coupon_button.click()
    coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
    coupon_code_textbox.send_keys("CNUPCE")
    User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
    User_per_customer_button.click()
    custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
    custom_select.click()
    discount_amount_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_discount_value_et")))
    discount_amount_textbox.send_keys("1254")
    min_order_amount = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/flat_min_order_value_et")))
    min_order_amount.send_keys("")
    driver.hide_keyboard()
    try:
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))


def test_clicking_on_back_button_from_create_coupon_page_should_ask_for_confirmation(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    flat_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Flat discount")')))
    flat_coupon_button.click()
    coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
    coupon_code_textbox.send_keys("CNUPCE")
    back_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView")))
    back_button.click()
    assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Leave")')))


def test_create_bxgy_with_coupon_code_empty(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView")))
    bxgy_coupon_button.click()
    coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
    coupon_code_textbox.send_keys("")
    User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
    User_per_customer_button.click()
    custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
    custom_select.click()
    click_buy_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextBuy")))
    click_buy_in_coupon_details.send_keys(1)
    click_get_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextGet")))
    click_get_in_coupon_details.send_keys(2)
    driver.hide_keyboard()
    try:
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))


def test_create_bxgy_with_users_per_customer_as_empty(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView")))
    bxgy_coupon_button.click()
    driver.hide_keyboard()
    click_buy_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextBuy")))
    click_buy_in_coupon_details.send_keys(1)
    click_get_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextGet")))
    click_get_in_coupon_details.send_keys(2)
    driver.hide_keyboard()
    try:
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))


def test_create_bxgy_with_buy_coupon_details_as_empty(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView")))
    bxgy_coupon_button.click()
    coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
    coupon_code_textbox.send_keys("")
    User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
    User_per_customer_button.click()
    custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Custom")')))
    custom_select.click()
    click_get_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextGet")))
    click_get_in_coupon_details.send_keys(2)
    driver.hide_keyboard()
    try:
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))


def test_create_bxgy_with_get_coupon_details_as_empty(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView")))
    bxgy_coupon_button.click()
    driver.hide_keyboard()
    click_buy_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextBuy")))
    click_buy_in_coupon_details.send_keys(1)
    driver.hide_keyboard()
    try:
        driver.assertEqual(driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Create coupon")').is_displayed(), True)

    except Exception as e:
        logger.error("Extra charge not deleted" + str(e))
        logger.info("Extra charge deleted successfully" + str(e))


# COMMENT
def test_create_bxgy_for_specific_product(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView")))
    bxgy_coupon_button.click()
    coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
    coupon_code_textbox.send_keys("AASHSJKJ")
    User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
    User_per_customer_button.click()
    custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Unlimited")')))
    custom_select.click()
    click_buy_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextBuy")))
    click_buy_in_coupon_details.send_keys(1)
    click_get_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextGet")))
    click_get_in_coupon_details.send_keys(2)
    driver.hide_keyboard()
    click_apply_coupon_on = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/couponOptionTv")))
    click_apply_coupon_on.click()
    click_specific_product = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Specific products")')))
    click_specific_product.click()
    click_select_product = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/productsTV")))
    click_select_product.click()
    click_search_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Search']")))
    click_search_icon.click()
    search_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("Search")')))
    search_icon.send_keys("Test")
    # click_search_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Search']")))
    # click_search_icon.send_keys("Tea")
    click_test_product = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.CheckBox")))
    click_test_product.click()
    click_test_product1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.CheckBox")))
    click_test_product1.click()
    click_add_products = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/add_prod_tv")))
    click_add_products.click()
    assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Testproduct1,Testproduct")')))


def test_create_bxgy_for_specific_categories(appium_driver):
    driver = appium_driver
    logincall = LoginPage(driver)
    logincall.logincall()
    manage_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Manage")')))
    manage_icon.click()
    discount_coupons_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Small Icon"])[3]')))
    discount_coupons_icon.click()
    create_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/action_btn")))
    create_coupon_button.click()
    bxgy_coupon_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView")))
    bxgy_coupon_button.click()
    coupon_code_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/coupon_code_et")))
    coupon_code_textbox.send_keys("AASHSJKJ")
    User_per_customer_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Select uses per customer")')))
    User_per_customer_button.click()
    custom_select = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Unlimited")')))
    custom_select.click()
    click_buy_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextBuy")))
    click_buy_in_coupon_details.send_keys(1)
    click_get_in_coupon_details = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/editTextGet")))
    click_get_in_coupon_details.send_keys(2)
    driver.hide_keyboard()
    click_apply_coupon_on = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/couponOptionTv")))
    click_apply_coupon_on.click()
    choose_specific_categories = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Specific categories")')))
    choose_specific_categories.click()
    click_specific_categories = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/productsTV")))
    click_specific_categories.click()
    click_categories = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Electronic")')))
    click_categories.click()
    add_categories = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Add 1 categories")')))
    add_categories.click()
    assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Electronic")')))

# def test_create_bxgy_for_all_product(appium_driver):

# if '__main__' == __name__:
#   pytest.main()
