from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.LoginPage import login1
from Utilities.readproperties import Readconfig
from PageObjects.AddCustPage import AddCust


class Test_AddCust:
    url = Readconfig.geturl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()

    def test_AddCust_002(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = login1(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.ac = AddCust(self.driver)
        self.ac.Click_OutCustomers()
        self.ac.Click_InCustomers()
        self.ac.Click_Add_New()
        self.ac.Enter_Email("monika1@gmail.com")
        self.ac.Enter_Password("monika123")
        self.ac.Enter_FirstName("Monika")
        self.ac.Enter_LastName("Somwanshi")
        self.ac.Select_Gender()
        self.ac.Click_DOB("2/5/1994")
        self.ac.Enter_Company("Magna")
        self.driver.find_element(By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@aria-expanded='true']").send_keys("Test Store 2")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[normalize-space()='Test store 2']").click()
        time.sleep(2)
        self.ac.Select_Vendor(1)
        self.ac.Click_Save_Button()
        self.ac.Add_Cust_Status()

        if self.ac.Add_Cust_Status() == True:
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\NoCommerce Demo "
                                        "Project\\ScreenShots\\AddCust_Fail.png")
            assert False
