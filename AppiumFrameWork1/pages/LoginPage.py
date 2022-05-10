from itertools import product

from AppiumFrameWork.main.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator for loginpage

    _getstartbutton = "com.dukaan.app:id/get_started"  # id
    _clickemailbutton = "com.dukaan.app:id/btn_email"  # id
    _enteremailadddress = "com.dukaan.app:id/et_input"  # id
    _continueemailbutton = "com.dukaan.app:id/btn_continue"  # id
    _enterpassword = "com.dukaan.app:id/et_password"  # id
    _continuepassbutton = "com.dukaan.app:id/btn_continue"  # id
    _veriftyhomepage = "com.dukaan.app:id/home"  # id
    _orderPage = "com.dukaan.app:id/navigation_bar_item_icon_view"  # id
    _assert = "Home"  # text

    def getStartMethod(self):
        self.clickElement(self._getstartbutton, "id")

    def clickEmailButton(self):
        self.clickElement(self._clickemailbutton, "id")
        return

    def enterEmailAddress(self):
        self.sendText("cojeret739@kuruapp.com", self._enteremailadddress, "id")

    def clickEmailContinueButton(self):
        self.clickElement(self._continueemailbutton, "id")

    def enterPassword(self):
        self.sendText("dukaanauto", self._enterpassword, "id")

    # def enterPassword2(self):
    # self.sendText("Clinton@971", self._enterpassword, "id")

    def clickPasswordContinueButton(self):
        self.clickElement(self._continuepassbutton, "id")

    def verifyHomePage(self):
        self.clickElement(self._veriftyhomepage, "id")

    def order(self):
        self.clickElement(self._orderPage, "id")

    def asserts(self):
        self.clickElement(self._assert, "text")

    def logincall(self):
        self.getStartMethod()
        self.clickEmailButton()
        self.enterEmailAddress()
        self.clickEmailContinueButton()
        self.enterPassword()
        self.clickPasswordContinueButton()
        self.verifyHomePage()
