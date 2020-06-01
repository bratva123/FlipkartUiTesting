from utilities.selenium_driver import SeleniumDriver
import base.customLogger as cl
import logging
import  time

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _popUpLogin = "//div[@class='_1XBjg- row']"
    _email_field = "(//div[@class='Km0IJL col col-3-5']//input)[1]"
    _password_field = "(//div[@class='Km0IJL col col-3-5']//input)[2]"
    _login_button = "//span[contains(text(),'Login')]/ancestor::button"
    _myAccount = "//div[contains(text(),'My Account')]"
    _wrongPswEmail = "//span[contains(text(),'Your username or password is incorrect')]"
    _emptyField = "//span[contains(text(),'Please enter valid Email ID/Mobile number')]"

    def clickLoginLink(self):
        time.sleep(2)
        self.elementClick("//a[contains(text(),'Login')]", locatorType="xpath")
    def enterEmail(self, email):
        time.sleep(10)
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType='xpath')

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        bol = self.isElementPresent(self._popUpLogin, locatorType="xpath")
        print(bool)
        if bool:
            self.enterEmail(email)
            self.enterPassword(password)
            self.clickLoginButton()
        else:
            self.clickLoginLink()
            self.enterEmail(email)
            self.enterPassword(password)
            self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._myAccount,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._wrongPswEmail,
                                       locatorType="xpath")
        return result

        return result
    def verifyEmptyField(self):
        result = self.isElementPresent(self._emptyField,
                                       locatorType="xpath")
        return result

