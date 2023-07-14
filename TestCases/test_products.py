import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from PageObjects.LoginPage import login1
from PageObjects.ProductsPage import Products
from Utilities.readproperties import Readconfig


class Test_Products:
    url = Readconfig.geturl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()

    def test_product_Name_003(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = login1(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.cl = Products(self.driver)
        self.cl.Click_Catalog()
        self.cl.Click_Products()
        # self.cl.Click_Search_Field()
        self.cl.Enter_Product_Name("macbookk")
        time.sleep(2)
        self.cl.Click_Search_Btn()

        if self.cl.Product_search_Result() == True:
            print(self.cl.Product_search_Result())
            self.lp.Click_Logout()
            assert True
        else:
            self.cl.Product_Not_available()
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\NoCommerce Demo "
                                        "Project\\ScreenShots\\ProductSearch.png")
            assert False
