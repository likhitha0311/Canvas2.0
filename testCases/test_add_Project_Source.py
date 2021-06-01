from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.customLogger import Loggen
from utilities.readProperties import ReadConfig
from utilities import XLUtils
from pageObjects.LoginPage import LoginPage

class Test_11_add_Project_Source:
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData//Logindata.xlsx"
    logger = Loggen.log_generator()

    def test_add_Project_Source(self,setUp):
        self.driver=setUp
        self.lp=LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()

        time.sleep(3)
        self.lp.clickElement("link_Project_linktext")
        time.sleep(5)
        self.lp.clickElement("link_firstelement")
        time.sleep(3)
        self.lp.clickElement("link_sourceinsideproject")
        time.sleep(3)
        row = XLUtils.getRowCount(self.path, "AddProjectSource")

        time.sleep(3)

        for r in range(2, row + 1):
            SourceType = XLUtils.readData(self.path, "AddProjectSource", r, 3)
            Contact = XLUtils.readData(self.path, "AddProjectSource", r, 4)

            Status  = XLUtils.readData(self.path, "AddProjectSource", r, 5)
            Notes=XLUtils.readData(self.path, "AddProjectSource", r, 6)

            Totalsourceitems = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
            for each_element in Totalsourceitems:
                if each_element.text == "No records to display":
                    initial_count = 0
                    print("Ïnitial count  is", initial_count)
                    break
                else:
                    initial_count = len(Totalsourceitems)
                    print("Ïnitial count  is", initial_count)

            self.lp.clickElement("button_addprojectsource")
            self.lp.clickElement("drop_sourcetype_xpath")
            SourcTypelist = self.driver.find_elements(By.XPATH, "//div[@id='project_source_type_codess_tree']//li")
            self.lp.selectfromdropdown(SourcTypelist, SourceType)
            self.lp.clickElement("label_source")

            self.lp.clickElement("drop_sourcecontact")
            self.driver.find_element(By.XPATH, "//input[@aria-owns='contactList_options']").send_keys(Contact)
            time.sleep(2)
            Contactnameslist = self.driver.find_elements(By.XPATH, "//div[@id='contactList_popup']//li")
            # self.lp.selectfromdropdown(Contactnameslist,Contact)
            for every_contact in Contactnameslist:
                if Contact in every_contact.text:
                    every_contact.click()
                    break

            self.lp.clickElement("drop_sourcestatus_xpath")
            project_source_status = self.driver.find_elements(By.XPATH,
                                                              "//div[@id='project_source_status_codeee_popup']//ul/li")
            self.lp.selectfromdropdown(project_source_status,Status)

            self.lp.sendKeys("text_sourceinsideprojectnotes",Notes)
            time.sleep(2)
            self.lp.clickElement("button_submitsource")

            time.sleep(2)
            try:
                wait = WebDriverWait.until(
                    EC.presence_of_element_located(By.XPATH, "(//a[@id='kt_quick_panel_close'])[1]"))
                print("Project Source not added due to missing data")
                self.logger.error("Project Source not added due to missing data")

            except:
                final_count = len(self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr"))
                if final_count == initial_count + 1:
                    print("Project Source added successfully")
                    self.logger.info("Project Source added successfully")
                else:
                    print("Project Source not added successfully")
                    self.logger.error("Project Source not added successfully")

        self.driver.close()




