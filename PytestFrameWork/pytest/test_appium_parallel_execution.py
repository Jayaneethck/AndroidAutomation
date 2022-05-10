import time

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PytestFrameWork.pytest.conftest import appium_driver
import random

name = ['Rahul', 'Arjun', 'Ravi', 'Hari', 'Nikhil', 'Sachin', 'Suresh', 'Manu', 'Rishi', 'Varun', 'Prithwi', 'Ajil']


def test_do_login(appium_driver):
    driver = appium_driver
    time.sleep(2)
    get_started_button = driver.find_element_by_id("com.dukaan.app:id/get_started")
    get_started_button.click()
    time.sleep(2)
    continue_with_email_button = driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
    continue_with_email_button.click()
    time.sleep(2)
    email_address_textbox = driver.find_element_by_id("com.dukaan.app:id/et_input")
    email_address_textbox.send_keys("clintonvinoth77@gmail.com")
    time.sleep(2)
    continue_button = driver.find_element_by_id("com.dukaan.app:id/btn_continue")
    continue_button.click()
    time.sleep(2)
    password_textbox = driver.find_element_by_id("com.dukaan.app:id/et_password")
    password_textbox.send_keys("Clinton@97")
    time.sleep(2)
    enter_password_button = driver.find_element_by_id("com.dukaan.app:id/btn_continue")
    enter_password_button.click()
    time.sleep(2)
    account_icon = driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("Account")')
    account_icon.click()
    time.sleep(2)
    additional_information = driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("Additional Information")')
    additional_information.click()
    time.sleep(2)
    sigh_out = driver.find_element_by_id("com.dukaan.app:id/logout_ll")
    sigh_out.click()
    time.sleep(2)
    assert driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("Sign Out")')


def test_edit_business_name(appium_driver):
    business_name_text = random.choice(name)
    driver = appium_driver
    time.sleep(2)
    get_started_button = driver.find_element_by_id("com.dukaan.app:id/get_started")
    get_started_button.click()
    time.sleep(2)
    continue_with_email_button = driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("Continue with Email")')
    continue_with_email_button.click()
    time.sleep(2)
    email_address_textbox = driver.find_element_by_id("com.dukaan.app:id/et_input")
    email_address_textbox.send_keys("clintonvinoth77@gmail.com")
    time.sleep(2)
    continue_button = driver.find_element_by_id("com.dukaan.app:id/btn_continue")
    continue_button.click()
    time.sleep(2)
    password_textbox = driver.find_element_by_id("com.dukaan.app:id/et_password")
    password_textbox.send_keys("Clinton@97")
    time.sleep(2)
    enter_password_button = driver.find_element_by_id("com.dukaan.app:id/btn_continue")
    enter_password_button.click()
    time.sleep(2)
    accounts_icon = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
    accounts_icon.click()
    edit_details_text = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Edit business details")')))
    edit_details_text.click()
    business_name_textbox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/store_name_et")))
    business_name_textbox.send_keys(business_name_text)
    save_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/email_et")))
    save_button.click()
    assert WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Store details updated")')))
