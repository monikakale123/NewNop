import pytest
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCust:
    Click_OutCustomers_XPATH = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    Click_InCustomers_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Click_Add_New_XPATH = (By.XPATH, "//a[@class='btn btn-primary']")
    Text_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@id='FirstName']")
    Text_LastName_XPATH = (By.XPATH, "//input[@id='LastName']")
    Select_Gender_XPATH = (By.XPATH, "//input[@id='Gender_Male']")
    Click_Calender_XPATH = (By.XPATH, "//span[@class='k-icon k-i-calendar']")
    Open_Cal_XPATH = (By.NAME, "DateOfBirth")
    Enter_DOB_XPATH = (By.XPATH, "//input[@id='DateOfBirth']")
    Text_Company_XPATH = (By.XPATH, "//input[@id='Company']")
    Click_Newsletter_XPATH = (By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']")
    Select_Vendor1_XPATH = (By.XPATH, "//select[@id='VendorId']")
    Click_Save_Button_XPATH = (By.XPATH, "//button[@name='save']")
    Add_cust_Status_XPATH = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")

    def __init__(self, setup):
        self.driver = setup

    def Click_OutCustomers(self):
        self.driver.find_element(*AddCust.Click_OutCustomers_XPATH).click()

    def Click_InCustomers(self):
        self.driver.find_element(*AddCust.Click_InCustomers_XPATH).click()

    def Click_Add_New(self):
        self.driver.find_element(*AddCust.Click_Add_New_XPATH).click()

    def Enter_Email(self, email):
        self.driver.find_element(*AddCust.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*AddCust.Text_Password_XPATH).send_keys(password)

    def Enter_FirstName(self, firstname):
        self.driver.find_element(*AddCust.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_LastName(self, lastname):
        self.driver.find_element(*AddCust.Text_LastName_XPATH).send_keys(lastname)

    def Select_Gender(self):
        self.driver.find_element(*AddCust.Select_Gender_XPATH).click()

    def Click_Calender(self):
        self.driver.find_element(*AddCust.Click_Calender_XPATH).click()

    def Open_Calender(self):
        self.driver.find_element(*AddCust.Open_Cal_XPATH).click()

    def Click_DOB(self, dob):
        self.driver.find_element(*AddCust.Enter_DOB_XPATH).send_keys(dob)

    def Enter_Company(self, company):
        self.driver.find_element(*AddCust.Text_Company_XPATH).send_keys(company)

    def Click_Newsletter(self, new):
        try:
            newsletter = Select(self.driver.find_element(*AddCust.Click_Newsletter_XPATH))
            newsletter.select_by_index(new)
        except UnexpectedTagNameException:
            pass

    def Select_Vendor(self, ven):
        Vendor = Select(self.driver.find_element(*AddCust.Select_Vendor1_XPATH))
        Vendor.select_by_index(ven)

    def Click_Save_Button(self):
        self.driver.find_element(*AddCust.Click_Save_Button_XPATH).click()

    def Add_Cust_Status(self):
        try:
            self.driver.find_element(*AddCust.Add_cust_Status_XPATH).text
            return True
        except NoSuchElementException:
            return False
