from pageObjects.BasePage import BasePage
from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage


class ContactsPage(BasePage):
    def __init__(self, driver):
        self.driver=driver


