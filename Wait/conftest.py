import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    #setup: open chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit() #teardown:close browser