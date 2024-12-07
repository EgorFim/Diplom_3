import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from selenium import webdriver
from data import test_url,BASE_URL,STATIC_DATA,DRIVER_NAME
import requests

@pytest.fixture
def user():
    response = requests.post(f'{BASE_URL}auth/register', json=STATIC_DATA)
    yield response
    r = response.json()['accessToken']
    requests.delete(f'{BASE_URL}auth/user', headers={'authorization':f'{r}'})


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
    else:
        DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()


@pytest.fixture
def driver_get(driver):
    driver.get(test_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.ZAGRUZKA_GLAVNOI))
    return driver


