import allure

@allure.title("Google Search Test")
@allure.description("Verify that Google home page opens and title contains 'Google'")
def test_google_search(driver):  # <-- 'driver' comes from fixture
    with allure.step("Open Google"):
        driver.get("https://www.google.com/")

    with allure.step("Verify page title contains 'Google'"):
        assert "Google" in driver.title, "Title does not contain 'Google'"
