import unittest

import pytest
import self as self

from AppiumFrameWork.pages.LoginPage import LoginPage
from AppiumFrameWork.pages.AccountPage import AccountPage
import AppiumFrameWork.utilities.CustomLogger as cl

from AppiumFrameWork.tests.conftest import beforeMethod


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class orderTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classobjects1(self):
        self.cf = LoginPage(self.driver)
        self.ap = AccountPage(self.driver)

    def test_edit_business_name(self):
        self.cf.logincall()
        self.ap.editbusinessdetail()

    def test_update_store_logo(self):
        self.cf.logincall()
        self.ap.updatestorelogo()





