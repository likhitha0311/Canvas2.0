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


class Test_13_Bulk_Edit:

    path = ".//TestData//Logindata.xlsx"
    logger=Loggen.log_generator()

    def test_bulk_edit(self,setUp):
        self.driver = setUp
        self.lp = BasePage(self.driver)
        time.sleep(3)

        self.lp.clickElement("link_Project_linktext")
        time.sleep(6)
        checkboxes=self.driver.find_elements(By.XPATH, "(//div[@class='e-checkbox-wrapper e-css'])")
        for i in range(1,4):
            self.driver.execute_script("arguments[0].click();", checkboxes[i])

       # self.lp.clickElement("checkbox1")
       # self.lp.clickElement("checkbox2")
        #self.lp.clickElement("checkbox3")
        self.lp.clickElement("pen")
        time.sleep(2)
        self.lp.clickElement("bulkeditfield")
        time.sleep(2)
        self.lp.clickElement("publisheddate")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[@class='e-input-group-icon e-date-icon e-icons']").click()
        time.sleep(2)
        self.lp.clickElement("popup_today_xpath")
        time.sleep(2)
        self.lp.clickElement("updateprojects")
        date1=self.driver.find_element(By.XPATH,"(//tbody/tr[1]/td[6])[2]").text
        print(date1)
        date2=self.driver.find_element(By.XPATH,"(//tbody/tr[2]/td[6])").text
        print(date2)
        date3=self.driver.find_element(By.XPATH, "(//tbody/tr[3]/td[6])").text
        print(date3)

        time.sleep(2)
        if date1== date2== date3:
            print("Bulk edit working correctly")
        else:
            print("Bulk edit not working correctly")




