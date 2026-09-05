from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "wrongpassword")
    page.click("button[type='submit']")

    assert "Your password is invalid!" in page.content()
    print("Wrong password test passed!")

    browser.close()