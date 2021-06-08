from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.ContactsPage import ContactsPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test_003_Search:
    baseurl=ReadConfig.getUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    path="./TestData/Logindata.xlsx"
    search_contact_value=XLUtils.readData(path,"SearchContact",2, 1)
    search_company_value = XLUtils.readData(path, "SearchCompany", 2, 1)
    search_project_value = XLUtils.readData(path, "SearchProject", 2, 1)

    def test_contact_search(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        time.sleep(5)
        #self.contact=ContactsPage(self.driver)
        self.lp.clickElement("link_Contacts_linktext")
        time.sleep(7)
        self.lp.sendKeys("txt_Search_name", self.search_contact_value)
        self.driver.find_element(By.NAME,'search').send_keys(Keys.ENTER)
        time.sleep(5)
        listofresults=self.driver.find_elements(By.XPATH, "//tr//td[3]")
        print(len(listofresults))
        for each_element in listofresults:
            text=each_element.text
            if self.search_contact_value in text:
                print("Contact search result is correct",text )
            else:
                print("Incorrect Contact search result found", text)

        self.driver.close()

    def test_company_search(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        time.sleep(5)
        self.lp.clickElement("link_Companies_linktext")
        time.sleep(7)
        self.lp.sendKeys("txt_Search_name", self.search_company_value)
        self.driver.find_element(By.NAME,'search').send_keys(Keys.ENTER)
        time.sleep(5)
        listofresults=self.driver.find_elements(By.XPATH, "//tr//td[3]")
        print(len(listofresults))
        for each_element in listofresults:
            text=each_element.text
            if self.search_company_value in text:
                print("Company search result is correct",text )
            else:
                print("Incorrect Company search result found", text)

        self.driver.close()

    def test_project_search(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        time.sleep(5)
        self.lp.clickElement("link_Project_linktext")
        time.sleep(7)
        self.lp.sendKeys("txt_Search_name", self.search_project_value)
        self.driver.find_element(By.NAME,'search').send_keys(Keys.ENTER)
        time.sleep(5)
        listofresults=self.driver.find_elements(By.XPATH, "//tr//td[3]")
        print(len(listofresults))
        for each_element in listofresults:
            text=each_element.text
            if self.search_project_value in text:
                print("Project search result is correct",text )
            else:
                print("Incorrect Project search result found", text)

        self.driver.close()


