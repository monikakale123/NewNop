import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get("https://admin-demo.nopcommerce.com/")
    return driver

    # driver.close()
