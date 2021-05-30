import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By

#configparser is package
#RawConfigParser is class
#config is the object

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")
config.sections()

class ReadConfig:



 @staticmethod
 def getUsername():
    username=config.get('Common info', 'username')
    return username

 @staticmethod
 def getPassword():
     password= config.get('Common info', 'password')
     return password

 @staticmethod
 def getUrl():
     baseurl = config.get('Common info', 'baseurl')
     return baseurl

 @staticmethod
 def getWebElement(locator1):
     textbox_username_name = config.get('WebElements', locator1)
     #print(textbox_username_name)

     #tuple(textbox_username_name)

     ''''
     locatorType =textbox_username_name.split(":")[0]
     print("Locator type is "+locatorType)
     locatorvalue= textbox_username_name.split(":")[1]
     print("Locator value is" + locatorvalue)
     if locatorType.__contains__('xpath'):
             locator =(By.XPATH, locatorvalue)


     elif locatorType.__contains__('name'):
            print("Am i Coming inside elif " + locatorType)
            locator = ('By.NAME', locatorvalue)
            print(By.NAME)
            print(locator)

     '''
     return textbox_username_name

