from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig

class BasePage2():
 def __init__(self, driver):
    self.driver = driver

 def getByType (self, locatorType):
    locatorType = locatorType.lower()
    if locatorType == "id":
        return By.ID
    elif locatorType == "name":
        print("Name is ")
        return By.NAME
    elif locatorType == "xpath":
        return By.XPATH
    elif locatorType == "css":
        return By.CSS_SELECTOR
    elif locatorType == "class":
        return By.CLASS_NAME
    elif locatorType == "link":
        return By.LINK_TEXT
    else:
        print("Locator type ", locatorType, " not correct/supported")
        return False

 def getElement(self, locatorType,locator):
        element = None
        try:
            print("Am I coming inside getElement")
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            print(byType)
            element = self.driver.find_element(byType, locator)
            print("Element Found with locator: ", locator, " and locatorType: ", locatorType)
        except:
            print("Element not found with locator: ", locator, " and  locatorType: ", locatorType)
        return element

#def sendKeys(self, data, locator, locatorType="id"):
 def sendKeys(self,locator,data):



            print("data is " +data)
            #print("Username  is " + locator)

            #value_and_locatortype = ()
            value_and_locatortype = ReadConfig.getWebElement(locator)
            res = eval(value_and_locatortype)
            print(res)
            '''
            self.value_and_locatortype = self.value_and_locatortype.replace('(', '')
            self.value_and_locatortype = self.value_and_locatortype.replace(')', '')
            #print(self.value_and_locatortype)
            self.index1 = self.value_and_locatortype.split(",")[0]
            #self.index1=self.index1.split(".")[1]
            #print(self.index1)
            self.index2 = self.value_and_locatortype.split(",")[1]
            #print(self.index2)
            ele = (self.index1,self.index2)
            # print(ele)
            #element = self.getElement(self.index1, self.index2)
            
            print(locator)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).send_keys(data)
            '''
            #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(res)).send_keys(data)
            self.driver.find_element(*res).send_keys(data)
            #element.send_keys(data)
            #print("Sent data on element with locator: " , self.index2 , " locatorType: " , self.index1)


            #print("Cannot send data on the element with locator: " , self.index2 , " locatorType: " , self.index1)
            #print("Cannot send data on the element with locator")

 def clickElement(self,locator):
     element=ReadConfig.getWebElement(locator)
     res=eval(element)
     print(res)
     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(res)).click()

