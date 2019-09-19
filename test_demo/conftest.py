import pytest

@pytest.yield_fixture(scope='module')
def setUpClass():
    print("open the browser")
    print('enter the url')
    yield
    print('close browser')

@pytest.fixture()
def setUpMethod():
    print('login')
    yield
    print('logout')