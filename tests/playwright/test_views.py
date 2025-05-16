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
        assert page.title() == "be kind club"
        assert page.locator("a.info-link", has_text="Mehr Info").is_visible()

        # Test the info page
        page.locator("a.info-link").click()
        assert page.url == "http://127.0.0.1:8000/info/"
        page.wait_for_selector("h1", timeout=1000)
        assert page.locator("h1").is_visible()

        # Test the questionnaire page
        page.goto("http://127.0.0.1:8000/questionnaire/")
        assert page.locator("h2").is_visible()  # Ensure the question header is visible

        # Answer all questions in the questionnaire dynamically
        while page.url == "http://127.0.0.1:8000/questionnaire/":
            page.locator("button[value='A']").click()

        # Test the result page
        assert page.url == "http://127.0.0.1:8000/calculate_result/", "Navigation to result page failed"
        page.wait_for_selector("h1", timeout=1000)
        assert page.locator("h1", has_text="Dein Ergebnis").is_visible()

        # Close the browser
        browser.close()