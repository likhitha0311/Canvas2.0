from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import randominfo
import random
import pytest



class Test_006_add_Contact:
    ''''
    baseurl=ReadConfig.getUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    '''
    path=".//TestData/Logindata.xlsx"
    logger=Loggen.log_generator()

    #@pytest.mark.skip
    def test_add_contact(self,setUp):
        ''''
        self.driver=setUp
        self.lp=LoginPage(self.driver)
        self.logger=Loggen.log_generator()
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.click_login()
        '''
        # first 2 lines newly added
        self.driver = setUp
        self.lp = BasePage(self.driver)
        time.sleep(3)

        self.lp.clickElement("link_Contacts_linktext")

        max_row=XLUtils.getRowCount(self.path,"AddContact")

        for r in range(2, max_row+1):
             FirstName=randominfo.get_first_name()
             LastName=randominfo.get_last_name()
             Email=self.lp.random_char(6)
             LeadSource=XLUtils.readData(self.path,"AddContact", r, 6)
             ContactNumber=XLUtils.readData(self.path,"AddContact", r, 6)

             time.sleep(3)
             self.lp.clickElement("button_addacontact_xpath")
             self.lp.sendKeys("txt_firstname_xpath",FirstName)
             self.lp.sendKeys("txt_lastname_xpath", LastName)
             self.lp.sendKeys("txt_email_xpath", Email+"@gmail.com")
             self.lp.clickElement("popup_calender_xpath")
             self.lp.clickElement("popup_startdate_xpath")
             self.lp.sendKeys("txt_leadsource_xpath",LeadSource)
             self.lp.sendKeys("text_contactnumber_xpath",ContactNumber)
             self.lp.clickElement("button_addcontact_xpath")

             time.sleep(3)
             contacttext=self.driver.find_element(By.XPATH, "(//tr[1]/td[3])[2]").text
             if FirstName in contacttext:
                 print( "Contact added successfully")
                 self.logger.info("Contact added successfully")

                 ''''
                 self.lp.clickElement("link_firstelement")
                 self.lp.clickElement("link_firstelement")
                 time.sleep(2)
                 self.lp.clickElement("button_plus")
                 self.lp.clickElement("link_delete")
                 time.sleep(1)
                 self.lp.clickElement("button_yes")
                 time.sleep(2)
                 self.lp.sendKeys("txt_Search_name", FirstName+" "+LastName)
                 self.driver.find_element(By.NAME, 'search').send_keys(Keys.ENTER)
                 time.sleep(3)
                 try:
                     wait1 = WebDriverWait(self.driver, 10)
                     wait1.until(EC.presence_of_element_located((By.XPATH, "//td[.='No records to display']")))
                     # self.driver.find_element(
                     print("Contact has been deleted successfully")
                     self.logger.info("Contact has been deleted successfully")

                 except:
                     print("Contact has not been deleted successfully")
                     self.logger.info("Contact has not been deleted successfully")
                     '''
             else:
                print("Contact not  added successfully")
                self.logger.error("Contact not added successfully")

        self.driver.close()



    #@pytest.mark.skip
    def test_add_company_inside_contact(self,setUp):
        ''''
        self.driver=setUp
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        '''
        #time.sleep(3)
        #first 2 lines newly added
        self.driver = setUp
        self.lp = BasePage(self.driver)

        time.sleep(3)
        self.lp.clickElement("link_Contacts_linktext")
        time.sleep(5)
        self.lp.clickElement("link_firstelement")
        self.lp.clickElement("link_firstelement")
        time.sleep(2)
        self.lp.clickElement("link_companies")

        r = XLUtils.getRowCount(self.path, "AddCompany")

        time.sleep(5)
        for row in range(2, r + 1):
            CompanyName=XLUtils.readData(self.path,"AddCompany",r,3)
            Email=self.lp.random_char(4)+"@gmail.com"
            ContactNumber=123456788
            Designation="software engineer"

            Totalcompanies = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
            initial_count=len(Totalcompanies)
            print("Initial count is ",  initial_count)

            self.lp.clickElement("button_associatenewcompany")
            self.lp.sendKeys("txt_email_xpath",Email)
            time.sleep(1)

            self.lp.clickElement("drop_companyname")
            self.driver.find_element(By.XPATH, "//input[@aria-owns='companyList_options']").send_keys(CompanyName)
            time.sleep(2)
            companylist=self.driver.find_elements(By.XPATH,"//div[@id='companyList_popup']//div/ul/li")
            self.lp.selectfromdropdown(companylist,CompanyName)
            time.sleep(2)

            self.lp.sendKeys("text_designation", Designation)
            self.lp.sendKeys("text_contactnumber_xpath", ContactNumber)
            self.lp.clickElement("popup_calender_xpath")
            self.lp.clickElement("popup_today_xpath")
            self.lp.clickElement("cbox_activecompany")
            time.sleep(1)
            self.lp.clickElement("button_addcontact_xpath")
            time.sleep(2)

            try:
                wait = WebDriverWait(self.driver, 1)
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@id='kt_quick_panel_close'])[2]")))
                print("Company not associated due to missing data")
                self.logger.error("Company not associated due to missing data")

            except:

                final_count=len(self.driver.find_elements(By.XPATH,"//table[@class='e-table']//tr"))
                if final_count == initial_count+1:

                    print("Company is associated  with contact successfully")
                    self.logger.info("Company is associated  with contact successfully")
                    time.sleep(2)
                    active_company=self.driver.find_element(By.XPATH, "//a[@title='Company']").text
                    #print(active_company)

                    if CompanyName in active_company:
                        print("Company is located in active position of contact successfully")
                        self.logger.info("Company is located in active position of contact successfully")
                    else:
                        print("Company  is not located in active position of contact successfully")
                        self.logger.error("Company is not located in active position of contact successfully")


        self.driver.close()


















