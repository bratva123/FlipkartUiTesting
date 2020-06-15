import unittest
import os
import HtmlTestRunner
from tests.searchResultTest import SearchResultTest
from tests.loginTest import LoginTests

dir = os.getcwd()


search = unittest.TestLoader().loadTestsFromTestCase(SearchResultTest)
login = unittest.TestLoader().loadTestsFromTestCase(LoginTests)


test_suite = unittest.TestSuite([login, search])

outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

runner = HtmlTestRunner.HTMLTestRunner(stream=outfile)

runner.run(test_suite)