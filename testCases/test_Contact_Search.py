from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.ContactsPage import ContactsPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time


class Test_003_Contact_Search:
    baseurl=ReadConfig.getUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    path="./TestData/Logindata.xlsx"
    search_contact_value=XLUtils.readData(path,"Contact",2,1)

    def test_contact_search(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        time.sleep(5)
        self.contact=ContactsPage(self.driver)
        self.contact.clickElement("link_Contacts_linktext")
        time.sleep(3)
        self.contact.sendKeys("txt_Search_name", self.search_contact_value)



