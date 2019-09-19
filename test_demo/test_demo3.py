from selenium import webdriver
import logging
def testMethod5(setUpMethod,setUpClass):
    print('modify another user')

def testMethod6(setUpMethod,setUpClass):
    driver=webdriver.Chrome()
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    logging.info('delete another user')