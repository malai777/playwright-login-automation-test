from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    assert "You logged into a secure area" in page.content()
    print("Login test passed!")

    browser.close()