from playwright.sync_api import sync_playwright

def test_index_page():
    """
    Test the index page of the be kind club application.
    """
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the index page
        page.goto("https://www.club.bekindstudio.at/")  # Replace with the correct URL if necessary

        # Check if the "Mehr Info" link is present and functional
        mehr_info_link = page.locator("a.info-link", has_text="Mehr Info")
        assert mehr_info_link.is_visible()
        mehr_info_link.click()
        assert page.url == "https://www.club.bekindstudio.at/info/"  # Replace with the correct URL if necessary

        # Navigate back to the index page
        page.goto("https://www.club.bekindstudio.at/")

        # Check if the "Klasse suchen" button is present and functional
        klasse_suchen_button = page.locator("a.next-button", has_text="Klasse suchen")
        assert klasse_suchen_button.is_visible()
        klasse_suchen_button.click()
        assert page.url == "https://www.club.bekindstudio.at/questionnaire/"  # Replace with the correct URL if necessary

        # Close the browser
        browser.close()