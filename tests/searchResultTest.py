import unittest
import pytest
import tests.login_tests
from pages.search.SearchPage import SearchPage
from base.conftest import oneTimeSetUp, setUp

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SearchResultTest(unittest.TestCase):

    _keyword = "Headphone"
    _wrongKeyword = "lkjhjhbs;fb;jsdfbdf"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SearchPage(self.driver)


    @pytest.mark.run(order=5)
    def test_validKeyword(self):
        self.sp.search(self._keyword)
        result = self.sp.isThereAnyResult()
        assert result == False

    @pytest.mark.run(order=4)
    def test_invalidKeyword(self):
        self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        self.sp.search(self._wrongKeyword)
        result = self.sp.isThereAnyResult()
        assert result == True
