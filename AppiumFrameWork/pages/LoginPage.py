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
    _orderPage = "com.dukaan.app:id/navigation_bar_item_icon_view" #id

    def getStartMethod(self):
        self.clickElement(self._getstartbutton, "id")
        cl.allureLogs("click on getStartMethod")


    def clickEmailButton(self):
        self.clickElement(self._clickemailbutton, "id")
        cl.allureLogs("click on emailButton")

    def enterEmailAddress(self):
        self.sendText("clintonvinoth97@gmail.com", self._enteremailadddress, "id")
        cl.allureLogs("Entered EmailAddress")

    def clickEmailContinueButton(self):
        self.clickElement(self._continueemailbutton, "id")
        cl.allureLogs("click on emailContinueButton")

    def enterPassword(self):
        self.sendText("Clinton@97", self._enterpassword, "id")
        cl.allureLogs("Entered Password")

    def enterPassword2(self):
        self.sendText("Clinton@971", self._enterpassword, "id")

    def clickPasswordContinueButton(self):
        self.clickElement(self._continuepassbutton, "id")
        cl.allureLogs("click on passWordContinueButton")


    def verifyHomePage(self):
        self.clickElement(self._veriftyhomepage, "id")
        cl.allureLogs("verifyHomePage")

    def order(self):
        self.clickElement(self._orderPage, "id")

