from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.hamropatro.com"
        self.rashifal_tab = (By.XPATH, "//a[@href='/rashifal']")

    def open(self):
        """Open Hamro Patro homepage"""
        self.driver.get(self.url)

    def click_rashifal(self, timeout=15):
        """Click on the Rashifal tab"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(self.rashifal_tab))
        element.click()
