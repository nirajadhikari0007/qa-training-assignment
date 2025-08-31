import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Setup and teardown for Chrome WebDriver"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
