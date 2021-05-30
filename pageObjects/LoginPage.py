from pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    #textbox_username_name = (By.NAME, 'email')
    textbox_password_name = "password"
    button_Login_xpath = "//button[.='Sign In']"
    link_Logout_id = 'kt_quick_user_toggle'
    link_Logout_linktext= 'Sign Out'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        #self.driver.find_element_by_name(self.textbox_username_name).clear()
        #self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)
        #self.sendKeys(Allthelocatorvalues.textbox_username_name, username)
        self.clearBox("textbox_username_name")
        self.sendKeys("textbox_username_name", username)



    def setPassword(self, password):
        #self.driver.find_element_by_name(self.textbox_password_name).clear()
        #self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)
        self.clearBox("textbox_password_name")
        self.sendKeys("textbox_password_name", password)

    def click_login(self):
        #self.driver.find_element_by_xpath(self.button_Login_xpath).click()
        self.clickElement("button_Login_xpath")

    def click_logout(self):
        self.clickElement("link_Logout_id")
        self.clickElement("link_Logout_linktext")


