from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.BasePage import BasePage
from utilities.readProperties import ReadConfig
from utilities import XLUtils
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
import time
import random


class Test_007_add_LineItem:
    ''''
    baseurl=ReadConfig.getUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    '''
    path=".//TestData//Logindata.xlsx"
    logger=Loggen.log_generator()

    def test_add_lineitem(self,setUp):
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


        row=XLUtils.getRowCount(self.path, "AddLineItem")
        for r in range(2,row+1):
             lineitem=XLUtils.readData(self.path, "AddLineItem", r,3)
             description=XLUtils.readData(self.path, "AddLineItem", r,4)
             amount=XLUtils.readData(self.path, "AddLineItem", r, 5)
             quantity=XLUtils.readData(self.path, "AddLineItem", r,6)

             Totallineitems = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
             for each_element in Totallineitems:
                 print(each_element.text)
                 if each_element.text == "No records to display":
                     initial_count = 0
                     print("Initial Count is ", initial_count)
                     break
                 else:
                     initial_count = len(Totallineitems)
                     print("Initial Count is ", initial_count)

             self.lp.clickElement("button_addlineitem")
             self.lp.clickElement("drop_lineitem")
             time.sleep(1)
             lineitemlist=self.driver.find_elements(By.XPATH, "//div[@id='order_item_codeee_tree']/ul/li")
             self.lp.selectfromdropdown(lineitemlist,lineitem)
             time.sleep(1)
             self.lp.sendKeys("textarea_description",description)
             #self.lp.clickElement("lineitemlabel")
             self.lp.sendKeys("text_orderamount", amount)
             self.lp.sendKeys("text_orderquantity", quantity)

             self.lp.clickElement("button_add_xpath")
             time.sleep(2)
             try:
                 wait=WebDriverWait(self.driver,2)
                 wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@id='kt_quick_panel_close'])[2]")))
                 #self.driver.find_element_by_xpath("(//a[@id='kt_quick_panel_close'])[2]")
                 print("Line item not added due to missing data")
                 self.logger.error("Line item not added due to missing data")
             except:
                 Totallineitems_add = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
                 final_count=len(Totallineitems_add)

                 if  final_count==initial_count+1:
                     print("Line item added successfully")
                     self.logger.info("Line item added successfully")

                 else:
                     print("Line item not added successfully")
                     self.logger.error("Line item not added successfully")
        self.driver.close()