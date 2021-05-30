import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
     baseurl=ReadConfig.getUrl()
     username=ReadConfig.getUsername()
     #print(username)
     password=ReadConfig.getPassword()
     #print(password)

     def test_login(self,setUp):
        self.driver=setUp
        self.lp=LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()



