import pytest
from selenium import webdriver

@pytest.yield_fixture(scope='function')
def perPostMethod(request,browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get('http://localhost/login.do')
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get('http://localhost/login.do')

    if request.cls is not None:
        request.cls.driver=driver

    yield driver
    driver.close()



def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
