from telnetlib import EC

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from AppiumFrameWork.main.BasePage import BasePage
from AppiumFrameWork.main.DriverClass import Driver
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator for login case
    _clickaccountbuttonicon = "com.dukaan.app:id/account"  # id
    _clickeditbusinessdetail = "com.dukaan.app:id/businessDetailsTV"  # id
    _enterbusinessname = "com.dukaan.app:id/store_name_et" #id
    _clicksavebutton = "com.dukaan.app:id/email_et" #id
    _clickupdatelogobutton = "com.dukaan.app:id/store_image_pick_rl" #id
    _clickgalleryicon = "android.widget.ImageView" #class

    def clickAccounticonButton(self):
        self.clickElement(self._clickaccountbuttonicon, "id")

    def clickBusinessDetails(self):
        self.clickElement(self._clickeditbusinessdetail, "id")

    def enterBusinessName(self):
        self.sendText("dukaan",self._enterbusinessname, "id")

    def clickSaveButton(self):
        self.clickElement("com.dukaan.app:id/email_et", "id")

    def clickUpdateLogoButton(self):
        self.clickElement("com.dukaan.app:id/store_image_pick_rl","id")

    def clickGalleryIcon(self):
        self.clickElement("android.widget.ImageView", "class")

    def editbusinessdetail(self):
        self.clickAccounticonButton()
        self.clickBusinessDetails()
        self.enterBusinessName()
        self.clickSaveButton()
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("dukaan")')

    def updatestorelogo(self):
        accounts_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Account")')))
        accounts_icon.click()
        edit_business_details_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Varun")')))
        edit_business_details_button.click()
        update_logo_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/tvSelectImage")))
        update_logo_button.click()
        gallery_icon = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Gallery")')))
        gallery_icon.click()
        folder_select = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.XPATH, "	//android.widget.ImageView[@content-desc='Folder']")))
        folder_select.click()
        image_select = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/image_view")))
        image_select.click()
        save_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, "com.dukaan.app:id/email_et")))
        save_button.click()
        assert WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("Store details updated")')))


