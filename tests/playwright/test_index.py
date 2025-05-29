from playwright.sync_api import sync_playwright

def test_index_page():
    """
    Test the index page of the Yogi application.
    """
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=True)  # Use headless=True for CI or debugging
        page = browser.new_page()

        # Define the base URL for local testing
        base_url = "http://127.0.0.1:8000"

        # Navigate to the index page
        page.goto(f"{base_url}/")

        # Navigate back to the index page
        page.goto(f"{base_url}/")

        # Check if the "Starte das Quiz" button is present and functional
        quiz_starten_button = page.locator("a", has_text="Starte das Quiz")
        assert quiz_starten_button.is_visible(), "Starte das Quiz button is not visible"
        quiz_starten_button.click()
        assert page.url == f"{base_url}/questionnaire/", "Navigation to questionnaire page failed"

        # Close the browser
        browser.close()