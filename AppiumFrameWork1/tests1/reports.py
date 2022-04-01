import unittest
import os
import test_accountpage
# import test_homepage
# Import the HTMLTestRunner Module
import HtmlTestRunner

from AppiumFrameWork1.tests import test_homepage, test_managepage, test_orderpage, test_productpage
from AppiumFrameWork1.tests1 import test_loginpage

"""import test_loginpage
import test_managepage
import test_orderpage
import test_productpage"""

# Get the Present Working Directory since that is the place where the report
# would be stored

current_directory = os.getcwd()


class HTML_TestRunner_TestSuite(unittest.TestCase):

    def test_automation_android(self):
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(accountpage.AccountPage),
            '''unittest.defaultTestLoader.loadTestsFromTestCase(test_homepage.HomePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_loginpage.LoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_managepage.ManageStorePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_orderpage.OrdersPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_productpage.ProductsPage)'''

           ])

        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )

        html_runner.run(consolidated_test)


if __name__ == '__main__':
    unittest.main()
