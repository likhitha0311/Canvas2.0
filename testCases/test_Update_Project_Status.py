from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import operator

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time

class Test_12_update_project_status:
    path = ".//TestData//Logindata.xlsx"
    logger = Loggen.log_generator()

    def test_update_project_status(self,setUp):
        self.driver=setUp
        self.lp=BasePage(self.driver)
        time.sleep(3)
        self.lp.clickElement("link_Project_linktext")
        time.sleep(6)
        self.lp.clickElement("link_firstelement")
        time.sleep(3)

        max_row = XLUtils.getRowCount(self.path, "ChangeProjectStatus")
        for r in range(2, max_row + 1):
            ProjectStatus = XLUtils.readData(self.path, "ChangeProjectStatus", r, 3)
            Notes=XLUtils.readData(self.path, "ChangeProjectStatus", r, 4)
            self.lp.clickElement("projectstatus_dropdown")
            time.sleep(1)
            project_status = self.driver.find_elements(By.XPATH, "//div[@id='status_code_popup']//ul/li")
            # self.lp.selectfromdropdown(project_status, ProjectStatus)

            for every_element in project_status:
                statustext = every_element.text
                if statustext == ProjectStatus:
                    self.driver.execute_script("arguments[0].click();", every_element)
                    break

            b=self.driver.find_element(By.XPATH, "(//ejs-sidebar[@id='sidebar-menu'])[1]").is_displayed()
            print(b)
            if b:
                self.lp.sendKeys("textarea_note", Notes)
                time.sleep(1)
                self.lp.clickElement("button_addactivity")
            else:
                pass

            time.sleep(2)
            Status_text=self.driver.find_element(By.XPATH, "(//select[@name='status_code']/option)[1]").get_attribute('value')

            if "-" in Status_text:
                Status_text=Status_text.replace("-"," ")
            else:
                pass


            if Status_text.lower() == ProjectStatus.lower():
                print("Project status is successfully changed")
                self.logger.info("Project status is successfully changed")
            else:
                print("Project status change-FAIL")
                self.logger.error("Project status change-FAIL")




