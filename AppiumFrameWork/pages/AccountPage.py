from AppiumFrameWork.main.BasePage import BasePage
from AppiumFrameWork.main.DriverClass import Driver


class orderPage(BasePage):

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


