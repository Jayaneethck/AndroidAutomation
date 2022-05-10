import unittest

import pytest
import self as self

from AppiumFrameWork.pages.LoginPage import LoginPage
from AppiumFrameWork.pages.AccountPage import orderPage
import AppiumFrameWork.utilities.CustomLogger as cl

from AppiumFrameWork.tests.conftest import beforeMethod


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class orderTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classobjects1(self):
        self.op = orderPage(self.driver)
        self.cf = LoginPage(self.driver)

    def test_edit_business_name(self):
        cl.allureLogs("App Launch")
        self.cf.getStartMethod()
        self.cf.clickEmailButton()
        self.cf.enterEmailAddress()
        self.cf.clickEmailContinueButton()
        self.cf.enterPassword()
        self.cf.clickPasswordContinueButton()
        self.cf.verifyHomePage()
        self.op.clickAccounticonButton()
        self.op.clickBusinessDetails()
        self.op.enterBusinessName()
        self.op.clickSaveButton()
        assert self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("Store details updated")')

    def test_update_store_logo(self):
        cl.allureLogs("App Launch")
        self.cf.getStartMethod()
        self.cf.clickEmailButton()
        self.cf.enterEmailAddress()
        self.cf.clickEmailContinueButton()
        self.cf.enterPassword()
        self.cf.clickPasswordContinueButton()
        self.cf.verifyHomePage()
        self.op.clickAccounticonButton()
        self.op.clickBusinessDetails()
        self.op.clickUpdateLogoButton()
        self.op.clickGalleryIcon()
