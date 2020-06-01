from utilities.selenium_driver import SeleniumDriver
import base.customLogger as cl
import logging
import  time

class SearchPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchField = "//input[@class='LM6RPg']"
    _searchBtn = "//button[@class='vh79eN']"
    _noResult = "//div[contains(text(),'Sorry, no results found!')]"

    def enterSearchKeyword(self, keyword):
        self.sendKeys(keyword, self._searchField, locatorType="xpath")

    def clickSearchButton(self):
        self.elementClick(self._searchBtn, locatorType="xpath")
        time.sleep(5)

    def search(self, keywords):
        self.enterSearchKeyword(keywords)
        self.clickSearchButton()

    def isThereAnyResult(self):
        result = self.isElementPresent("//div[@class='_1VpLOp']", locatorType="xpath")
        return result