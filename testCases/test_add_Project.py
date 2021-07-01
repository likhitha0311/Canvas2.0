from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import Select
from utilities import XLUtils
import time
import random


class Test_006_Add_Project:
    ''''
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    '''
    path = ".//TestData//Logindata.xlsx"
    logger=Loggen.log_generator()

    def test_add_project(self,setUp):
        '''
        self.driver=setUp
        self.lp=LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        '''
        self.driver = setUp
        self.lp = BasePage(self.driver)
        time.sleep(3)

        max_row=XLUtils.getRowCount(self.path,"AddProject")

        for r in range(2,max_row+1):
           ProjectName=self.lp.random_char(4)+"Project"
           ProjectType=XLUtils.readData(self.path,"AddProject",r,4)
           ProjectStatus=XLUtils.readData(self.path,"AddProject",r,5)
           Address=XLUtils.readData(self.path,"AddProject",r,6)
           City=XLUtils.readData(self.path,"AddProject",r,7)
           Country=XLUtils.readData(self.path,"AddProject",r,8)
           ProjectSourceType=XLUtils.readData(self.path,"AddProject",r,9)
           SourceContact=XLUtils.readData(self.path,"AddProject",r,10)
           ProjectSourceStatus=XLUtils.readData(self.path,"AddProject",r,11)
           Notes=XLUtils.readData(self.path,"AddProject",r,12)

           self.lp.clickElement("link_Project_linktext")
           time.sleep(5)
           self.lp.clickElement("button_addnewproject_xpath")
           self.lp.sendKeys("txt_projectname_xpath", ProjectName)

           time.sleep(1)
           self.lp.clickElement("drop_ProjectType_xpath")
           ProjectTypeArrowlist = self.driver.find_elements(By.XPATH,
                                                 "//*[@id='project_type_tree']//div[@class='e-icons e-icon-expandable interaction']")
           for every_arrow in ProjectTypeArrowlist:
               time.sleep(1)
               #print("length of arrowlist", len(ProjectTypeArrowlist))
               every_arrow.click()


           time.sleep(3)
           projecttypeoptions=self.driver.find_elements(By.XPATH,"//div[@id='project_type_tree']//ul//li")
           self.lp.selectfromdropdown(projecttypeoptions, ProjectType)
           self.lp.clickElement("label_AddProject_xpath")

           self.lp.clickElement("drop_projectstatus_xpath")
           time.sleep(1)
           project_status = self.driver.find_elements(By.XPATH, "//div[@id='status_code_popup']//ul/li")
           #self.lp.selectfromdropdown(project_status, ProjectStatus)

           for every_element in project_status:
               statustext=every_element.text
               if statustext ==  ProjectStatus:
                   self.driver.execute_script("arguments[0].click();",every_element)
                   break

           self.lp.sendKeys("txtarea_address_xpath", Address)
           self.lp.sendKeys("txt_projectcity_xpath", City)

           self.lp.clickElement("drop_projectcountry_xpath")
           countrynames = self.driver.find_elements(By.XPATH, "//div[@id='country_code_popup']//ul/li")
           self.lp.selectfromdropdown(countrynames, Country)

           self.lp.sendKeys("textarea_notes_xpath", Notes)

           #time.sleep(1)
           self.lp.sendKeys("txt_projectdrivelink_xpath", "abcd.com")

           self.lp.sendKeys("txt_projectsourcedrivelink_xpath", "source.com")

           self.lp.clickElement("drop_sourcestatus_xpath")
           project_source_status = self.driver.find_elements(By.XPATH,
                                                             "//div[@id='project_source_status_code_popup']//ul/li")
           self.lp.selectfromdropdown(project_source_status, ProjectSourceStatus)

           time.sleep(1)
           self.lp.clickElement("drop_sourcetype_xpath")
           Arrowlist = self.driver.find_elements(By.XPATH,
                                                 "//*[@id='project_source_type_code_tree']//div[@class='e-icons e-icon-expandable interaction']")
           for every_arrow in Arrowlist:
               time.sleep(1)
               every_arrow.click()
           time.sleep(1)
           project_source_Type = self.driver.find_elements(By.XPATH,
                                                           "//div[@id='project_source_type_code_tree']/ul//li")
           self.lp.selectfromdropdown(project_source_Type, ProjectSourceType)
           self.lp.clickElement("label_AddProjectSource_xpath")

           time.sleep(1)
           self.lp.clickElement("drop_sourcecontact_xpath")
           time.sleep(2)
           #self.lp.sendKeys("txt_sourcecontact_xpath", SourceContact)
           #source_contact_matchinglist = self.driver.find_elements(By.XPATH, "//div[@id='contactList_popup']//ul/li")
           #self.lp.selectfromdropdown(source_contact_matchinglist, SourceContact)
           self.driver.find_element(By.XPATH, "//input[@aria-owns='contactList_options']").send_keys(SourceContact)
           time.sleep(3)
           Contactnameslist = self.driver.find_elements(By.XPATH, "//div[@id='contactList_popup']//ul/li")
           # self.lp.selectfromdropdown(Contactnameslist,Contact)
           print(len(Contactnameslist))
           for every_contact in Contactnameslist:
               print(every_contact.text)
               if SourceContact in every_contact.text:
                   self.driver.execute_script("arguments[0].click();", every_contact)
                   break

           time.sleep(2)


           self.lp.clickElement("button_addProject_xpath")

           time.sleep(3)
           projecttext = self.driver.find_element(By.XPATH, "(//tr[1]/td[3])[2]").text

           if projecttext == ProjectName:
              print("Project added successfully")
              self.logger.info("Project added successfully")
              self.lp.clickElement("link_firstelement")
              time.sleep(3)
              self.lp.clickElement("link_sourceinsideproject")
              time.sleep(5)
              source=self.driver.find_element(By.XPATH, "(//tr[1]/td[2])[2]").text
              if source in SourceContact:
                  print("Project source added successfully")
                  self.logger.info("Project source added successfully")

                  self.lp.clickElement("ellipses")
                  self.lp.clickElement("button_edit")
                  time.sleep(4)
                  print("****Update project source form*****")
                  print(self.lp.getText("drop_sourcetype_xpath"))
                  print(self.driver.find_element(By.XPATH, "//select[@name='contactList']/option").get_attribute('innerHTML'))
                  print(self.driver.find_element(By.XPATH, "//select[@name='project_source_status_codeee']/option").get_attribute('value'))
                  self.lp.clickElement("closebutton")
              else:
                  print("Project source not added successfully")
                  self.logger.error("Project source not added successfully")

           else:
              print("Project not added successfully")
              self.logger.error("Project not added successfully")

        self.driver.close()






