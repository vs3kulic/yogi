from playwright.sync_api import sync_playwright

def test_info_page():
    """
    Test the info page of the Yogi application and verify navigation to the questionnaire page.
    """
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=False)  # Use headless=False for debugging
        page = browser.new_page()

        # Navigate to the info page
        page.goto("https://www.club.bekindstudio.at/info/")  # Replace with the correct URL if necessary

        # Verify the page title
        assert page.title() == "Über Yogi", "Page title is incorrect"

        # Check if the header is displayed
        header = page.locator("h1")
        assert header.is_visible(), "Header is not visible"
        assert header.text_content() == "be kind club", "Header text is incorrect"

        # Check if the introductory text is present
        intro_text = page.locator("main p", has_text="Unser Yoga-Matcher hilft dir")  # Refined selector
        assert intro_text.is_visible(), "Introductory text is not visible"
        assert intro_text.text_content().strip().startswith(
            "Unser Yoga-Matcher hilft dir"
        ), "Introductory text is incorrect"

        # Verify that the "Los geht’s" button is present and functional
        los_gehts_button = page.locator("a.next-button", has_text="Los geht’s")
        assert los_gehts_button.is_visible(), "Los geht’s button is not visible"
        los_gehts_button.click()

        # Close the browser
        browser.close()