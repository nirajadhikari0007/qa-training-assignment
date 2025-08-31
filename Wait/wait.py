from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# implicit wait
driver.implicitly_wait(5)

driver.get("https://www.amazon.com/")

# Pop up handle (if nav-main exists)
try:
    driver.find_element(By.ID, "nav-main")
except:
    pass

# explicit wait for search box
wait = WebDriverWait(driver, 10)
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)

# Try search laptop
search_box.send_keys("Laptop")
search_box.submit()

# Explicit wait for search result
first_result = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
    )
)[0]  # get the first result

# get the title of first search result
title = first_result.find_element(By.TAG_NAME, "h2").text
print("First search result title:", title)

# Validate that laptop is in the title
assert "laptop" in title.lower()
print("Validation Passed: 'Laptop' found in the first search")

# close browser
driver.quit()
