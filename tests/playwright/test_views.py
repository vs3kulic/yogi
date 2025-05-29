from playwright.sync_api import sync_playwright

def test_views():
    """
    Test the main views of the Yogi app.
    """
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Test the index page
        page.goto("http://127.0.0.1:8000/")
        assert page.title() == "Be Kind Club - Find Your Perfect Yoga"

        # Test the questionnaire page
        page.goto("http://127.0.0.1:8000/questionnaire/")
        assert page.locator("h2").is_visible()  # Ensure the question header is visible

        # Test the result page
        page.goto("http://127.0.0.1:8000/result/")
        assert page.locator("h1", has_text="Dein Ergebnis").is_visible()

        # Close the browser
        browser.close()