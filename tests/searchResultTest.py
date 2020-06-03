import unittest
import pytest
from pages.search.SearchPage import SearchPage
from base.conftest import oneTimeSetUp, setUp
import time
from utilities.smtpMailServer import sendMail

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SearchResultTest(unittest.TestCase):

    _keyword = "Headphone"
    _wrongKeyword = "lkjhjhbs;fb;jsdfbdf"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SearchPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validKeyword(self):
        self.sp.search(self._keyword)
        time.sleep(3)
        result = self.sp.isThereAnyResult()
        assert result == False
        sendMail(recieverMail="lavkr0403@gmail.com")

    @pytest.mark.run(order=1)
    def test_invalidKeyword(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        self.sp.search(self._wrongKeyword)
        time.sleep(3)
        result = self.sp.isThereAnyResult()
        assert result == True
