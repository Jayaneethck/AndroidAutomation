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
