from selenium import webdriver
import pytest
import string
import random


@pytest.fixture(scope='session')
def get_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome()
    # driver.delete_all_cookies()
    yield driver
    driver.close()


@pytest.fixture()
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
