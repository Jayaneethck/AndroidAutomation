import time

import pytest

from AppiumFrameWork.main.DriverClass import Driver


@pytest.fixture(scope='class')
def beforeClass(request):
    print('before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Method')


@pytest.fixture()
def beforeMethod():
    print('before Method')
    yield
    print('After Method')




    ################################

    '''import time
    import unittest

    import pytest

    from AppiumFrameWork1.pages.DriverClass import Driver

    # from AppiumFrameWork1.pages.DriverClass1 import Driver1

    @pytest.fixture(scope='class')
    def beforeClass(request):
        print('before Method')
        driver1 = Driver()
        driver = driver1.getDriverMethod()
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
        time.sleep(5)
        print('After Method')

        print('before Method')
        driver1 = driver1.getDriverMethod1()
        if request.cls is not None:
            request.cls.driver1 = driver1
        yield driver1
        time.sleep(5)
        driver1.quit()
        print('After Method')

    @pytest.fixture()
    def beforeMethod():
        print('before Method')
        yield
        print('After Method')

    @pytest.fixture(scope='class')
    def beforeClass1(request):
        print('before Class')
        driver1 = Driver()
        driver1 = driver1.getDriverMethod()
        if request.cls is not None:
            request.cls.driver1 = driver1
        yield driver1
        time.sleep(5)
        driver1.quit()
        print('After Method')

    @pytest.fixture()
    def beforeMethod1():
        print('before Method')
        yield
        print('After Method')

    def tearDown(self):
        self.driver.quit()

    if '__main__' == __name__:
        unittest.main()'''

