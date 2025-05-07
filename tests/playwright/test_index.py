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

        # Check if the "Mehr Info" link is present and functional
        mehr_info_link = page.locator("a.info-link", has_text="Mehr Info")
        assert mehr_info_link.is_visible(), "Mehr Info link is not visible"
        mehr_info_link.click()
        assert page.url == f"{base_url}/info/", "Navigation to info page failed"

        # Navigate back to the index page
        page.goto(f"{base_url}/")

        # Check if the "Klasse suchen" button is present and functional
        klasse_suchen_button = page.locator("a.next-button", has_text="Klasse suchen")
        assert klasse_suchen_button.is_visible(), "Klasse suchen button is not visible"
        klasse_suchen_button.click()
        assert page.url == f"{base_url}/questionnaire/", "Navigation to questionnaire page failed"

        # Close the browser
        browser.close()