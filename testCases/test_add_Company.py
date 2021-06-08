import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage
from pageObjects.ContactsPage import ContactsPage
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import Loggen
import time
import randominfo
from utilities.customLogger import Loggen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Test_004_Add_Company:
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = "./TestData/Logindata.xlsx"
    logger = Loggen.log_generator()

    #@pytest.mark.skip
    def test_add_company(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseurl)
        self.login=LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.click_login()
        self.login.clickElement("link_Companies_linktext")
        r=XLUtils.getRowCount(self.path,"AddCompany")

        time.sleep(5)
        for row in range(2,r+1):
            #CompanyName=XLUtils.readData(self.path,"AddCompany",r,3)
            CompanyType=XLUtils.readData(self.path,"AddCompany",row,4)
            City=XLUtils.readData(self.path,"AddCompany",row,5)
            Country=XLUtils.readData(self.path,"AddCompany",row,6)
            CompanyName=self.login.random_char(8)+"Company"


            time.sleep(3)
            self.login.clickElement("button_addnewcompany_id")
            self.login.sendKeys("txt_CompanyName_xpath",CompanyName)
            time.sleep(1)
            self.login.clickElement("drop_IndustryType_xpath")
            items=self.driver.find_elements(By.XPATH,"//div[@id='industryType_tree']/ul/li")

            self.login.selectfromdropdown(items,CompanyType)
            self.login.clickElement("label_AddCompany_xpath")

            self.login.sendKeys("txt_city_xpath", City)
            self.login.clickElement("drop_country_xpath")
            countrynames=self.driver.find_elements(By.XPATH, "//ul[@id='country_options']/li")
            self.login.selectfromdropdown(countrynames,Country)
            self.login.clickElement("button_add_xpath")
            time.sleep(3)

            companytext=self.driver.find_element(By.XPATH, "(//tr[1]/td[3])[2]").text
            #print(companytext)
            if companytext == CompanyName:
                print("Company added successfully")
                self.logger.info("Company added successfully")
                self.login.clickElement("link_firstelement")
                time.sleep(2)
                self.login.clickElement("button_plus")
                self.login.clickElement("link_delete")
                time.sleep(1)
                self.login.clickElement("button_yes")
                time.sleep(2)
                self.login.sendKeys("txt_Search_name", CompanyName)
                self.driver.find_element(By.NAME,'search').send_keys(Keys.ENTER)
                time.sleep(3)
                try:
                     wait1 = WebDriverWait(self.driver, 10)
                     wait1.until(EC.presence_of_element_located((By.XPATH, "//td[.='No records to display']")))
                     #self.driver.find_element(
                     print("Company has been deleted successfully")
                     self.logger.info("Company has been deleted successfully")

                except:
                      print("Company has not been deleted successfully")
                      self.logger.info("Company has not been deleted successfully")
            else:
                print("Company not  added successfully")
                self.logger.error("Company not added successfully")

        self.driver.close()

    @pytest.mark.skip
    def test_add_contact_inside_company(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.click_login()
        time.sleep(3)
        self.login.clickElement("link_Companies_linktext")
        time.sleep(4)
        self.login.clickElement("link_firstelement")

        time.sleep(3)
        max_row = XLUtils.getRowCount(self.path, "AddContact")

        for r in range(2, max_row + 1):
            FirstName = randominfo.get_first_name()
            LastName = randominfo.get_last_name()
            Email = self.login.random_char(6)
            LeadSource = XLUtils.readData(self.path, "AddContact", r, 6)
            ContactNumber = XLUtils.readData(self.path, "AddContact", r, 6)

            Totalcontacts = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
            for each_element in Totalcontacts:
                if each_element.text == "No records to display":
                    initial_count = 0
                    print("Ïnitial count  is", initial_count)
                    break
                else:
                    initial_count = len(Totalcontacts)
                    print("Ïnitial count  is", initial_count)

            time.sleep(3)
            self.login.clickElement("button_addnewcontact")
            time.sleep(1)
            self.login.sendKeys("txt_firstname_xpath", FirstName)
            self.login.sendKeys("txt_lastname_xpath", LastName)
            self.login.sendKeys("txt_companycontactemail", Email + "@gmail.com")
            self.login.clickElement("drop_companycontactstartdate")
            self.login.clickElement("popup_today_xpath")
            self.login.sendKeys("txt_leadsource_xpath", LeadSource)
            self.login.sendKeys("text_companycontactphone", ContactNumber)
            self.login.clickElement("button_companycontactadd")
            time.sleep(2)


            try:
                wait=WebDriverWait(self.driver,2)
                wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@id='kt_quick_panel_close'])[2]")))
                print("Contact inside company not added due to missing data")
                self.logger.error("Contact inside company not added due to missing data")

            except:

                #Totalorderitems_add = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
                final_count = len(self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr"))
                print("Final count is " ,final_count)
                if final_count == initial_count + 1:
                        print("Contact added successfully inside company")
                        self.logger.info("Contact added successfully inside company")

                else:
                        print("Contact not added successfully")
                        self.logger.error("Contact not added successfully inside company")

        self.driver.close()











