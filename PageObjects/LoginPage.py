import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class login1:
    Text_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Click_Login_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_Logout_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self, setup):
        self.driver = setup

    def Enter_Email(self, email):
        self.driver.find_element(*login1.Text_Email_XPATH).clear()
        self.driver.find_element(*login1.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*login1.Text_Password_XPATH).clear()
        self.driver.find_element(*login1.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*login1.Click_Login_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*login1.Click_Logout_XPATH).click()



