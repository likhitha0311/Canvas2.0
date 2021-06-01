from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
import time
import randominfo


class Test_10_Add_Company_Role:
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/Logindata.xlsx"
    logger = Loggen.log_generator()

    # @pytest.mark.skip
    def test_add_contact(self, setUp):
        self.driver = setUp
        self.lp = LoginPage(self.driver)
        self.logger = Loggen.log_generator()
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        time.sleep(3)
        self.lp.clickElement("link_Project_linktext")
        time.sleep(5)
        self.lp.clickElement("link_firstelement")
        row = XLUtils.getRowCount(self.path, "AddCompanyRole")

        time.sleep(3)

        for r in range(2, row + 1):
           CompanyRole = XLUtils.readData(self.path, "AddCompanyRole", r, 3)
           Company = XLUtils.readData(self.path, "AddCompanyRole", r, 4)
           Contact = XLUtils.readData(self.path, "AddCompanyRole", r, 5)
            

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
           Roles=self.driver.find_elements(By.XPATH,"//div[@id='company_role_code_tree']//li//span")
           print(len(Roles))
           self.lp.selectfromdropdown(Roles,CompanyRole)

           self.lp.clickElement("drop_companyname")
           self.driver.find_element(By.XPATH,"//input[@aria-owns='company_code_options']").send_keys(Company)
           time.sleep(2)
           Companynameslist=self.driver.find_elements(By.XPATH,"//div[@id='company_code_popup']//li")
           #self.lp.selectfromdropdown( Companynameslist,Company)
           for ele in Companynameslist:
               if Company in ele.text:
                   ele.click()
                   break


           time.sleep(4)
           self.lp.clickElement("drop_contact")
           #time.sleep(2)
           self.driver.find_element(By.XPATH,"//input[@aria-owns='contact_code_options']").send_keys(Contact)
           time.sleep(2)
           Contactnameslist=self.driver.find_elements(By.XPATH,"//div[@id='contact_code_popup']//li")
           #self.lp.selectfromdropdown(Contactnameslist,Contact)
           for every_contact in Contactnameslist:
               if Contact in every_contact.text:
                   every_contact.click()
                   break

           time.sleep(2)
           self.lp.clickElement("button_submitcompanyrole")

           try:
               wait=WebDriverWait.until(EC.presence_of_element_located(By.XPATH,"(//a[@id='kt_quick_panel_close'])[1]"))
               print("Company Role not added due to missing data")
               self.logger.error("Company Role not added due to missing data")

           except:
               final_count=len(self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr"))
               if final_count == initial_count+1:
                    print("Company Role added successfully")
                    self.logger.info("Company Role added successfully")
               else:
                    print("Company Role not added successfully")
                    self.logger.error("Company Role not added successfully")

        self.driver.close()
                    
                   





        
                   








