def test_google_search(driver): # <-- 'driver' comes from fixture
    # with allure.step ("Open google home page")
    driver.get("https://www.google.com/")
    assert "Google" in driver.title, "Title doesnot contain 'Google'"