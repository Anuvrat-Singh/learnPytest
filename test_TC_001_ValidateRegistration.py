#fixture is pre requisite. global makes global setting. yield says it will execute after each test case. we need to pass fixture in each test



from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def setBrowser():
    print("using fixture to execute this before any test starts execution")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.close()



def test_registration_valid_data(setBrowser):
    url = "https://thetestingworld.com/testing"
    driver.get(url)
#    driver.close()
    assert driver.title == "Testing World Experienced in making experts"

def test_registration_invalid_data(setBrowser):
    url = "https://www.facebook.com/"
    driver.get(url)
#    driver.maximize_window()
#    driver.close()
    assert driver.current_url == "https://www.facebook.com/"


def test_invalid_data(setBrowser):
    url = "https://www.facebook.com/"
    driver.get(url)
#    driver.maximize_window()
#    driver.close()