from pyvirtualdisplay import Display
from selenium import webdriver
import os
from py._xmlgen import html
def oneTimeSetUp():
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('window-size=2000x2000')
        baseURL = "https://www.flipkart.com"
        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(5)
        # driver.set_window_size(1200,1200)
        driver.get(baseURL)
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



