from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the homepage
        page.goto("https://www.yogi.bekindstudio.at/")  # Replace with your deployed URL if testing in production

        # Check if the homepage title is correct
        assert page.title() == "Yogi sagt: Hallo!!"

        # Check if the "Kurs suchen" button exists
        assert page.locator("text=Klasse suchen").is_visible()

        # Click the "Los geht’s" button
        page.locator("text=Klasse suchen").click()

        # Verify that the questionnaire page is loaded
        assert page.url == "https://www.yogi.bekindstudio.at/questionnaire/"  # Adjust the URL if necessary

        # Close the browser
        browser.close()