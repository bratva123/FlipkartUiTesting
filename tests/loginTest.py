from pages.home.login_page import LoginPage
import unittest
import pytest
from base.conftest import oneTimeSetUp, setUp

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    email = "9931145329"
    password = "nishi@1234"

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.driver = oneTimeSetUp
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=3)
    def test_validLogin(self):
        self.lp.login(self.email, self.password)
        result = self.lp.verifyLoginSuccessful()
        assert result == True


    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        self.lp.login(self.email, "96623978")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=1)
    def test_emptyField(self):
        self.lp.login("","")
        result = self.lp.verifyEmptyField()
        assert result == True

if __name__ == '__main__':
    unittest.main()