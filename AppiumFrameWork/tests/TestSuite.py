import unittest
import pytest
from AppiumFrameWork.tests.logintest import LoginCall
from AppiumFrameWork.tests.test_accountcases import orderTest





cf = unittest.TestLoader().loadTestsFromTestCase(LoginCall)
gt = unittest.TestLoader().loadTestsFromTestCase(orderTest)

test = unittest.TestSuite(cf, gt)

unittest.TextTestRunner(verbosity=1).run(test)
