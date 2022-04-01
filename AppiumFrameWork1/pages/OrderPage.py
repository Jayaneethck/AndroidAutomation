import related as related
from attr import field

from AppiumFrameWork1.main.BaseClass import BasePage



class orderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locator for test_order_details_page in order page

    '''orders_icon = self.driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("Orders")')
    orders_icon.click()
    sleep(2)
    details_button = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Details")')
    details_button.click()
    sleep(2)
    assert self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("RECEIPT")')'''



    _ordericon = "com.dukaan.app:id/navigation_bar_item_icon_view" #id
    _detailbutton = "com.dukaan.app:id/orderItemTitle " #id



    def orderIcon(self):
        self.clickElement(self._ordericon, "id")

    def detailButton(self):
        self.clickElement(self._detailbutton, "id")

    def testOrderDetailsPage(self):
        self.orderIcon()
        self.detailButton()

