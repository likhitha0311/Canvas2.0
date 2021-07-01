from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time

class Test_008_add_deliverable:
    ''''
    baseurl=ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    '''
    path = ".//TestData//Logindata.xlsx"
    logger = Loggen.log_generator()
    
    def test_add_deliverable(self,setUp):
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
        time.sleep(5)
        self.lp.clickElement("link_Orders")
        time.sleep(3)
        self.lp.clickElement("link_1storder")
        time.sleep(2)
        self.lp.clickElement("link_Deliverables")
        
        row=XLUtils.getRowCount(self.path, "AddDeliverable")

        time.sleep(2)


        for r in range(2,row+1):
            deliverable = XLUtils.readData(self.path, "AddDeliverable", r, 3)
            description = XLUtils.readData(self.path, "AddDeliverable", r, 4)
            status = XLUtils.readData(self.path, "AddDeliverable", r, 5)
            status=status.lower()
            owner = XLUtils.readData(self.path, "AddDeliverable", r, 6)
            costcenter=XLUtils.readData(self.path, "AddDeliverable", r, 7)

            Totaldelitems = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
            for each_element in Totaldelitems:
                if each_element.text == "No records to display":
                    initial_count = 0
                    print("Ïnitial count  is", initial_count)
                    break
                else:
                    initial_count = len(Totaldelitems)
                    print("Ïnitial count  is", initial_count)

            self.lp.clickElement("button_adddeliverableitem")
            self.lp.clickElement("drop_deliverableitem")
            Deliverableitemslist = self.driver.find_elements(By.XPATH,
                                                                 "//div[@id='deliverable_item_codee_tree']/ul/li")
            self.lp.selectfromdropdown(Deliverableitemslist, deliverable)
            self.lp.clickElement("label_adddeliverable")

            self.lp.sendKeys("textarea_description", description)
            self.lp.sendKeys("textarea_note","dELIverable notes is added")

            self.lp.clickElement("drop_deliverablestatus")
            Deliverablestatuslist = self.driver.find_elements(By.XPATH,
                                                              "//div[@id='deliverable_status_codee_tree']/ul/li//div[@class='e-text-content']//span[@class='e-list-text']")
            for ele in Deliverablestatuslist:
                c=2;
                text = ele.get_attribute('innerHTML')
                if text.lower() == status:
                    self.driver.find_element(By.XPATH,"(//li[@data-uid='"+str(status)+"'])[%d]" %c).click()
                    break
            self.lp.clickElement("label_adddeliverable")

            #self.driver.find_element(By.XPATH,"(//li[@data-uid='open'])[2]").click()
            #print(len(Deliverablestatuslist))

            self.lp.clickElement("popup_calender_xpath")
            #time.sleep(1)
            self.lp.clickElement("popup_today_xpath")

            time.sleep(2)
            self.lp.clickElement("drop_costcenter")
            Deliverablecostlist = self.driver.find_elements(By.XPATH,"//div[@id='cost_center_code_popup']//ul/li")
            self.lp.selectfromdropdown(Deliverablecostlist, costcenter)
            self.lp.clickElement("label_adddeliverable")

            time.sleep(2)
            self.lp.clickElement("drop_deliverableowner")
            Deliverableownerlist = self.driver.find_elements(By.XPATH, "//div[@id='deliverable_owner_code_popup']//ul/li")
            self.lp.selectfromdropdown(Deliverableownerlist, owner)
            self.lp.clickElement("label_adddeliverable")

            #time.sleep(2)
            self.lp.clickElement("button_add_xpath")
            time.sleep(3)
            try:
                wait=WebDriverWait(self.driver,2)
                wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@id='kt_quick_panel_close'])[1]")))
                print("Deliverable not added due to missing data")
                self.logger.error("Deliverable not added due to missing data")

            except:

                Totaldelitems_add = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
                final_count = len(Totaldelitems_add)
                print("Final count is " ,final_count)
                if final_count == initial_count + 1:
                        print("Deliverable added successfully")
                        self.logger.info("Deliverable added successfully")

                else:
                        print("Deliverable not added successfully")
                        self.logger.error("Deliverable not added successfully")

        self.driver.close()




