import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    # setup: start browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver # <-- test runs here
    # Teardown: close browser
    driver.quit()