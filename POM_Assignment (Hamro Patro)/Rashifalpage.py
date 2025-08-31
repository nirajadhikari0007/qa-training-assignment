from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RashifalPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for Tula Rashi section
        self.tula_rashi = (By.XPATH, "//h3[contains(text(),'तुला')]")

    def is_tula_visible(self, timeout=10):
        """Check if Tula Rashi is visible"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(self.tula_rashi))
        return element.is_displayed()
