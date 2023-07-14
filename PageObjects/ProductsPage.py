import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import login1


class Products:
    Click_Catalogs_CSS = (By.CSS_SELECTOR, "body > div:nth-child(3) > aside:nth-child(2) > div:nth-child(2) > "
                                           "div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) "
                                           "> ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > p:nth-child(2)")
    Click_Products_XPATH = (By.XPATH, "//p[normalize-space()='Products']")
    Click_Search_Text_XPATH = (By.XPATH, "//div[@class='row search-row']")
    Text_Product_Name_XPATH = (By.XPATH, "//input[@id='SearchProductName']")
    Click_Search_Button_XPATH = (By.XPATH, "//button[@id='search-products']")
    Product_Search_Result_XPATH = (By.XPATH, "//a[normalize-space()='1']")
    Product_not_available_Link_Text = (By.LINK_TEXT, "No data available in table")


    def __init__(self, setup):
        self.driver = setup

    def Click_Catalog(self):
        self.driver.find_element(*Products.Click_Catalogs_CSS).click()

    def Click_Products(self):
        self.driver.find_element(*Products.Click_Products_XPATH).click()

    def Click_Search_Field(self):
        self.driver.find_element(*Products.Click_Search_Text_XPATH).click()

    def Enter_Product_Name(self, prod_name):
        self.driver.find_element(*Products.Text_Product_Name_XPATH).send_keys(prod_name)

    def Click_Search_Btn(self):
        self.driver.find_element(*Products.Click_Search_Button_XPATH).click()

    def Product_search_Result(self):
        try:
            self.driver.find_element(*Products.Product_Search_Result_XPATH)
            return True
        except NoSuchElementException:
            return False

    def Product_Not_available(self):
        self.driver.find_element(*Products.Product_not_available_Link_Text)
