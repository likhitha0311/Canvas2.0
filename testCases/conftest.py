from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
      driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser == 'firefox':
      driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver



def pytest_addoption(parser): #this will get the browser name from command line
    parser.addoption("--browser")


@pytest.fixture()#this will pass browser value to setup method
def browser(request):
    return request.config.getoption("--browser")

#aDDing envioronment info to html report
def pytest_configure(config):
    config._metadata['Project Name']='Canvas'
    #config._metadata['Module Name']='Admin'
    config._metadata['Tester']='Likhitha'

#ignoring default info from html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA-HOME", None)
    metadata.pop("Plugins", None)

