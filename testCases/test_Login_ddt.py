import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import Loggen
import time

class Test_002_Login_ddt:
    url=ReadConfig.getUrl()
    path="./TestData/Logindata.xlsx"
    logger=Loggen.log_generator()

    @pytest.mark.skip
    def test_login_ddt(self, setUp):
        self.driver=setUp
        self.lp=LoginPage(self.driver)
        self.driver.get(self.url)
        lst_status = []
        row=XLUtils.getRowCount(self.path,"Sheet1")

        for r in range(2,row+1):
            self.username = XLUtils.readData(self.path,"Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp=XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.click_login()
            time.sleep(5)
            act_title=self.driver.title
            exp_title= "Dashboard - Canvas"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.lp.click_logout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            print("Login DDT successfully completed")
            self.logger.info("Login DDT successfully completed")
        else:
            print("Login DDT failed")
            self.logger.error("Login DDT failed")
        self.driver.quit()












