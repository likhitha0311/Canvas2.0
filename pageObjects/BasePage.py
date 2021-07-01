from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
import random
import string
import time



class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def getText(self,locator):
        element = ReadConfig.getWebElement(locator)
        res = eval(element)
        text=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(res)).text
        return text



    def clickElement(self, locator):
        element = ReadConfig.getWebElement(locator)
        res = eval(element)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(res)).click()

    def sendKeys(self, locator, data):
        element = ReadConfig.getWebElement(locator)
        res = eval(element)
        #print(res)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(res)).send_keys(data)
        self.driver.find_element(*res).send_keys(data)

    def clearBox(self,locator):
        element = ReadConfig.getWebElement(locator)
        res = eval(element)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(res)).clear()
    ''''
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    '''

    def selectfromdropdown(self,dropdownlist, value):
        for each_element in dropdownlist:
            text=each_element.text
            #print(text)

            #text=each_element.get_attribute('innerHTML')
            #print(text.strip())

            ##text=each_element.get_attribute('value')
            ##print(text)
            if text == value:
                each_element.click()
                #self.driver.execute_script("arguments[0].click();", each_element)
                break



    def random_char(self,y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))




      

