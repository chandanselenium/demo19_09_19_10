from selenium import webdriver
from pom.loginpage import Loginpage
import pytest

@pytest.mark.usefixtures('perPostMethod')
class TestDemoOne():

    @pytest.fixture(autouse=True)
    def classobj(self,perPostMethod):
        self.lp = Loginpage(self.driver)


    def testValidLogin(self):

        self.lp.enterUsername('admin')
        self.lp.enterPassword('manager')
        self.driver.find_element_by_id('loginButton').click()
        self.lp.verifyTitle()
        #lp.clickLoginButton()

    def testValidLogin1(self):
        self.lp.enterUsername('admin')
        self.lp.enterPassword('manage')
        self.driver.find_element_by_id('loginButton').click()
        self.lp.verifyTitle()
