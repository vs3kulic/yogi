from playwright.sync_api import sync_playwright

def test_result_page():
    """
    This test checks the result page of the be kind club application.
    It verifies that the result page loads correctly and displays the expected content.
    """
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the result page (simulate a user completing the questionnaire)
        page.goto("https://www.club.bekindstudio.at/calculate_result/")  # Replace with your deployed URL if necessary

        # Check if the result header is displayed
        assert page.locator("h1").text_content() == "Dein Ergebnis"

        # Close the browser
        browser.close()