import pytest
from Homepage import HomePage
from Rashifalpage import RashifalPage

def test_tula_rashi_visible(driver):
    """Test that Tula Rashi is visible after navigating to Rashifal"""
    home = HomePage(driver)
    rashifal = RashifalPage(driver)

    # Step 1: Open homepage
    home.open()

    # Step 2: Click Rashifal tab
    home.click_rashifal()

    # Step 3: Validate Tula Rashi is visible
    assert rashifal.is_tula_visible(), "❌ Tula Rashi is not visible on Rashifal page"
