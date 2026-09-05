from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    # Leave username and password empty - just click submit
    page.click("button[type='submit']")

    assert "Your username is invalid!" in page.content()
    print("Empty fields test passed!")

    browser.close()