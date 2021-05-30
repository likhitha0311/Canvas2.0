from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils
from utilities.customLogger import Loggen
import time
import random

class Test_009_add_Order:
    baseurl=ReadConfig.getUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    path=".//TestData//Logindata.xlsx"
    logger=Loggen.log_generator()

    def test_add_Order(self,setUp):
        self.driver=setUp
        self.lp=LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()

        time.sleep(5)
        self.lp.clickElement("link_Companies_linktext")
        time.sleep(3)
        self.lp.clickElement("link_firstelement")
        time.sleep(3)
        self.lp.clickElement("link_OrdersinsideCompany")
        row=XLUtils.getRowCount(self.path,"AddOrder")

        time.sleep(3)


        for r in range(2, row+1):
            OrderName=self.lp.random_char(4)+"Order"
            print(OrderName)
            Notes =OrderName+XLUtils.readData(self.path, "AddOrder", r, 4)
            print(Notes)
            Amount=XLUtils.readData(self.path,"AddOrder",r,5)
            Currency=XLUtils.readData(self.path,"AddOrder",r,6)
            OrderOwner = XLUtils.readData(self.path, "AddOrder", r, 7)

            Totalorderitems = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
            for each_element in Totalorderitems:
                if each_element.text == "No records to display":
                    initial_count = 0
                    print("Ïnitial count  is", initial_count)
                    break
                else:
                    initial_count = len(Totalorderitems)
                    print("Ïnitial count  is", initial_count)

            self.lp.clickElement("button_addorder")
            time.sleep(3)
            self.lp.sendKeys("text_ordername", OrderName)
            self.lp.sendKeys("textarea_notes_xpath", Notes)
            self.lp.sendKeys("text_orderamount", Amount)
            self.lp.clickElement("drop_currency")
            currency_list=self.driver.find_elements(By.XPATH, "//div[@id='currency_code_popup']/div/ul/li")
            self.lp.selectfromdropdown(currency_list,Currency)
            self.lp.clickElement("label_addcompanyorder")

            self.lp.clickElement("text_validityfrom")
            self.lp.clickElement("popup_today_xpath")

            self.lp.clickElement("text_validitytill")
            self.lp.clickElement("popup_today_xpath")

            self.lp.clickElement("drop_orderowner")
            owner_list=self.driver.find_elements(By.XPATH,"//div[@id='order_owner_code_popup']//div//li")
            self.lp.selectfromdropdown(owner_list,OrderOwner)
            self.lp.clickElement("label_addcompanyorder")

            self.lp.clickElement("button_add_xpath")
            time.sleep(1)

            try:
                wait=WebDriverWait(self.driver,2)
                wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@id='kt_quick_panel_close'])[3]")))
                print("Order not added due to missing data")
                self.logger.error("Order not added due to missing data")

            except:

                Totalorderitems_add = self.driver.find_elements(By.XPATH, "//table[@class='e-table']//tr")
                final_count = len(Totalorderitems_add)
                print("Final count is " ,final_count)
                if final_count == initial_count + 1:
                        print("Order added successfully")
                        self.logger.info("Order added successfully")

                else:
                        print("Order not added successfully")
                        self.logger.error("Order not added successfully")






