from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import randominfo
import random
import pytest


class Test_12_Add_Contact_As_Project_Role:
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/Logindata.xlsx"
    logger = Loggen.log_generator()

    @pytest.fixture
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.click_login()
        yield
        self.driver.close()

    def test_add_Contact_As_Project_Role(self,setUp):
        time.sleep(4)
        self.lp.clickElement("link_Contacts_linktext")

        max_row = XLUtils.getRowCount(self.path, "AddContact")

        for r in range(2, max_row + 1):
            FirstName = randominfo.get_first_name()
            LastName = randominfo.get_last_name()
            Email = self.lp.random_char(6)
            LeadSource = XLUtils.readData(self.path, "AddContact", r, 6)
            ContactNumber = XLUtils.readData(self.path, "AddContact", r, 6)


            time.sleep(3)
            self.lp.clickElement("button_addacontact_xpath")
            self.lp.sendKeys("txt_firstname_xpath", FirstName)
            self.lp.sendKeys("txt_lastname_xpath", LastName)
            self.lp.sendKeys("txt_email_xpath", Email + "@gmail.com")
            self.lp.clickElement("popup_calender_xpath")
            self.lp.clickElement("popup_startdate_xpath")
            self.lp.sendKeys("txt_leadsource_xpath", LeadSource)
            self.lp.sendKeys("text_contactnumber_xpath", ContactNumber)
            self.lp.clickElement("button_addcontact_xpath")
            time.sleep(3)
            self.lp.clickElement("link_Project_linktext")
            time.sleep(5)
            self.lp.clickElement("link_firstelement")
            row = XLUtils.getRowCount(self.path, "AddCompanyRole")

            time.sleep(3)

            for r in range(2, row + 1):
                CompanyRole = XLUtils.readData(self.path, "AddCompanyRole", r, 3)
                Company = XLUtils.readData(self.path, "AddCompanyRole", r, 4)
                Contact =FirstName+" "+LastName

                Totaroleitems = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
                for each_element in Totaroleitems:
                    if each_element.text == "No records to display":
                        initial_count = 0
                        print("Ïnitial count  is", initial_count)
                        break
                    else:
                        initial_count = len(Totaroleitems)
                        print("Ïnitial count  is", initial_count)
                self.lp.clickElement("button_addcompanyrole")

                time.sleep(2)
                self.lp.clickElement("drop_companyrole")
                Roles = self.driver.find_elements(By.XPATH, "//div[@id='company_role_code_tree']//li")
                #print(len(Roles))
                self.lp.selectfromdropdown(Roles, CompanyRole)

                time.sleep(1)
                self.lp.clickElement("drop_contact")
                time.sleep(1)
                self.driver.find_element(By.XPATH, "//input[@aria-owns='contact_code_options']").send_keys(Contact)
                time.sleep(2)
                Contactnameslist = self.driver.find_elements(By.XPATH, "//div[@id='contact_code_popup']//li")

                for every_contact in Contactnameslist:
                    if Contact in every_contact.text:
                        every_contact.click()
                        break

                time.sleep(1)
                self.lp.clickElement("button_submitcompanyrole")
                time.sleep(1)

                try:
                    wait = WebDriverWait.until(
                        EC.presence_of_element_located(By.XPATH, "(//a[@id='kt_quick_panel_close'])[1]"))
                    print("Company Role not added due to missing data")
                    self.logger.error("Company Role not added due to missing data")

                except:
                    final_count = len(self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr"))
                    if final_count == initial_count + 1:
                        print("Company Role added successfully")
                        self.logger.info("Company Role added successfully")
                    else:
                        print("Company Role not added successfully")
                        self.logger.error("Company Role not added successfully")

            self.lp.clickElement("link_Contacts_linktext")
            time.sleep(5)
            self.lp.clickElement("link_firstelement")
            self.lp.clickElement("link_firstelement")
            time.sleep(3)
            self.lp.clickElement("link_projectsinsidecontact")
            time.sleep(3)
            final_project_count = len(self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr"))
            if  final_project_count == 1:
                print("Contact is associated with Project as role successfully")
                self.logger.info("Contact is associated with Project as role successfully")
            else:
                print("Contact is not associated with Project as role successfully")
                self.logger.error("Contact is not associated with Project as role successfully")



