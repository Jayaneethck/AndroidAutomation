import unittest

import pytest
import time
import random

from AppiumFrameWork.pages.LoginPage import LoginPage
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.pages.AccountPage import orderPage

product_names = ['Sauce', 'Sausage', 'Fire Extinguisher', 'Bagpack', 'Powder', 'Umbrella', 'Iphone', 'Charger']
category_names = ['Electronics', 'Household', 'Mobile Accessories', 'Food Items', 'Healthcare', 'Medical',
                  'Packed Foods', 'Skin Care', 'Mobile Phones', 'Clothing', 'Furniture', 'Beverage']
custom_color_codes = ['#FFFFFF', '#000000', "#FF0000", '#00FF00', '#0000FF', '#800080']


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginCall(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.cf = LoginPage(self.driver)
        self.op = orderPage(self.driver)

    def test_add_products(self):
        random_name = (random.choice(product_names))
        cl.allureLogs("App Launch")
        self.cf.getStartMethod()
        self.cf.clickEmailButton()
        self.cf.enterEmailAddress()
        self.cf.clickEmailContinueButton()
        self.cf.enterPassword()
        self.cf.clickPasswordContinueButton()
        self.cf.verifyHomePage()
        products_icon = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Products")')
        products_icon.click()
        time.sleep(2)
        add_product_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Add new product")')
        add_product_button.click()
        time.sleep(2)
        product_name = self.driver.find_element_by_id('com.dukaan.app:id/product_name_et')
        product_name.send_keys(random_name)
        time.sleep(2)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        continue_button.click()
        time.sleep(2)
        product_category_button = self.driver.find_element_by_id("com.dukaan.app:id/productCategoryET")
        product_category_button.click()
        time.sleep(2)
        self.driver.swipe(480, 1560, 491, 1049, 400)
        choose_category = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("sauce")')
        choose_category.click()
        time.sleep(2)
        select_button = self.driver.find_element_by_id("com.dukaan.app:id/selectButton")
        select_button.click()
        time.sleep(2)
        price_textbox = self.driver.find_element_by_id("com.dukaan.app:id/mrpET")
        price_textbox.send_keys("1000")
        discounted_price_textbox = self.driver.find_element_by_id("com.dukaan.app:id/sellingPriceET")
        discounted_price_textbox.send_keys("900")
        add_button = self.driver.find_element_by_id("com.dukaan.app:id/addUpdateProductButton")
        add_button.click()
        time.sleep(2)
        back_button = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        back_button.click()
        time.sleep(2)
        search_icon = self.driver.find_element_by_id("com.dukaan.app:id/search_icon")
        search_icon.click()
        time.sleep(2)
        search_textbox = self.driver.find_element_by_id("com.dukaan.app:id/search_et")
        search_textbox.send_keys(random_name)
        time.sleep(3)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("In stock")')

    def test_add_new_category(self):
        random_category_name = (random.choice(category_names))
        self.cf.getStartMethod()
        self.cf.clickEmailButton()
        self.cf.enterEmailAddress()
        self.cf.clickEmailContinueButton()
        self.cf.enterPassword()
        self.cf.clickPasswordContinueButton()
        self.cf.verifyHomePage()
        products_icon = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Products")')
        products_icon.click()
        time.sleep(2)
        categories_select = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Categories")')
        categories_select.click()
        time.sleep(2)
        add_categories_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Add new category")')
        add_categories_button.click()
        time.sleep(2)
        categories_textbox = self.driver.find_element_by_id("com.dukaan.app:id/name_et")
        categories_textbox.send_keys(random_category_name)
        time.sleep(2)
        create_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        create_button.click()
        time.sleep(4)
        search_icon = self.driver.find_element_by_id("com.dukaan.app:id/search_icon")
        search_icon.click()
        time.sleep(2)
        search_textbox = self.driver.find_element_by_id("com.dukaan.app:id/search_et")
        search_textbox.send_keys(random_category_name)
        time.sleep(2)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("In stock")')

    def test_add_products(self):
        random_name = (random.choice(product_names))
        cl.allureLogs("App Launch")
        self.cf.getStartMethod()
        self.cf.clickEmailButton()
        self.cf.enterEmailAddress()
        self.cf.clickEmailContinueButton()
        self.cf.enterPassword()
        self.cf.clickPasswordContinueButton()
        self.cf.verifyHomePage()
        products_icon = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Products")')
        products_icon.click()
        time.sleep(2)
        add_product_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Add new product")')
        add_product_button.click()
        time.sleep(2)
        product_name = self.driver.find_element_by_id('com.dukaan.app:id/product_name_et')
        product_name.send_keys(random_name)
        time.sleep(2)
        continue_button = self.driver.find_element_by_id("com.dukaan.app:id/action_btn")
        continue_button.click()
        time.sleep(2)
        product_category_button = self.driver.find_element_by_id("com.dukaan.app:id/productCategoryET")
        product_category_button.click()
        time.sleep(2)
        self.driver.swipe(480, 1560, 491, 1049, 400)
        choose_category = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("sauce")')
        choose_category.click()
        time.sleep(2)
        select_button = self.driver.find_element_by_id("com.dukaan.app:id/selectButton")
        select_button.click()
        time.sleep(2)
        price_textbox = self.driver.find_element_by_id("com.dukaan.app:id/mrpET")
        price_textbox.send_keys("1000")
        discounted_price_textbox = self.driver.find_element_by_id("com.dukaan.app:id/sellingPriceET")
        discounted_price_textbox.send_keys("900")
        add_button = self.driver.find_element_by_id("com.dukaan.app:id/addUpdateProductButton")
        add_button.click()
        time.sleep(2)
        back_button = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        back_button.click()
        time.sleep(2)
        search_icon = self.driver.find_element_by_id("com.dukaan.app:id/search_icon")
        search_icon.click()
        time.sleep(2)
        search_textbox = self.driver.find_element_by_id("com.dukaan.app:id/search_et")
        search_textbox.send_keys(random_name)
        time.sleep(3)
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("In stock")')
