from playwright.sync_api import sync_playwright

def test_info_page():
    """
    Test the info page of the Yogi application and verify navigation to the questionnaire page.
    """
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=True)  # Use headless=True for CI or debugging
        page = browser.new_page()

        # Define the base URL for local testing
        base_url = "http://127.0.0.1:8000"

        # Navigate to the info page
        page.goto(f"{base_url}/info/")

        # Verify the page title
        assert page.title() == "Über Yogi", "Page title is incorrect"

        # Check if the header is displayed
        page.wait_for_selector("h1", timeout=2000)  # Wait up to 2 seconds for the h1 element to appear
        header = page.locator("h1", has_text="be kind club")
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

        # Verify navigation to the questionnaire page
        assert page.url == f"{base_url}/questionnaire/", "Navigation to questionnaire failed"

        # Close the browser
        browser.close()