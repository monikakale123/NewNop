import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException

from Utilities.readproperties import Readconfig
from PageObjects.LoginPage import login1


class Test_login:
    url = Readconfig.geturl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()

    def test_Page_Title(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login_001(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = login1(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\NoCommerce Demo Project\\ScreenShots\\Login.png")
            assert False
