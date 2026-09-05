# playwright-login-automation-test

Playwright Login Automation Tests

A simple UI automation testing project built with Python and Playwright to demonstrate automated testing of a login page.

The tests use the The Internet
 demo application and cover positive and negative login scenarios.

🚀 Project Overview

This project demonstrates how Playwright can be used with Python to automate browser-based login tests.

The test suite currently covers:

✅ Successful login with valid credentials
❌ Login with an incorrect password
❌ Login with empty username and password fields

The project uses Playwright's synchronous Python API and Chromium for browser automation.

🛠️ Tech Stack
Python
Playwright
Chromium
The Internet - Herokuapp as the test application
📁 Project Structure
playwright-login-automation-test/
│
├── test_login.py
├── test_login_negative.py
├── test_login_empty.py
└── README.md

Test Files
test_login.py

Tests a successful login using valid credentials.

The test:

Opens the login page.
Enters the valid username.
Enters the valid password.
Submits the login form.
Verifies that the secure area is displayed.
test_login_negative.py

Tests login behavior when an incorrect password is provided.

The test verifies that the application displays:

Your password is invalid!

test_login_empty.py

Tests the login form with both username and password left empty.

The test verifies that the application displays:

Your username is invalid!

📋 Prerequisites

Make sure the following are installed:

Python 3.8+
pip
Git

Check your Python installation:

python --version


or:

python3 --version

🔧 Installation
1. Clone the repository
git clone https://github.com/malai777/playwright-login-automation-test.git

2. Navigate to the project
cd playwright-login-automation-test

3. Install Playwright
pip install playwright

4. Install Playwright browsers
playwright install


If you only want to install Chromium:

playwright install chromium

▶️ Running the Tests

Because the test files are written using Playwright's synchronous API, they can be executed directly with Python.

Run the successful login test
python test_login.py


Expected output:

Login test passed!

Run the invalid password test
python test_login_negative.py


Expected output:

Wrong password test passed!

Run the empty login test
python test_login_empty.py


Expected output:

Empty fields test passed!

🧪 Run All Tests

You can execute all three test files together:

python test_login.py && python test_login_negative.py && python test_login_empty.py

🔍 Test Scenarios
Test	Scenario	Expected Result
test_login.py	Valid username + valid password	Login succeeds
test_login_negative.py	Valid username + incorrect password	Password validation error
test_login_empty.py	Empty username + password	Username validation error
🔐 Test Credentials

The project uses the demo credentials provided by The Internet application:

Username: tomsmith
Password: SuperSecretPassword!


These credentials are for the public demo application and are not production credentials.

Security Note: Never commit real usernames, passwords, API keys, tokens, or other secrets to a public Git repository. For real-world automation projects, credentials should be stored using environment variables or a secure secrets manager.

🧩 How the Automation Works

The tests use Playwright to:

Launch Chromium
      ↓
Open Login Page
      ↓
Enter Credentials
      ↓
Submit Login Form
      ↓
Validate Expected Result
      ↓
Close Browser


For example, the successful login test launches Chromium and navigates to:

https://the-internet.herokuapp.com/login


It then interacts with the username and password fields and verifies that the secure area is displayed.

📌 Future Improvements

This project can be extended into a more complete Playwright automation framework by adding:

 Pytest integration
 Playwright fixtures
 Page Object Model (POM)
 HTML test reports
 Screenshots on test failure
 Video recording
 Headless/headed execution options
 Environment-based configuration
 Parameterized test data
 CI/CD integration with GitHub Actions
 Cross-browser testing with Chromium, Firefox, and WebKit
 Better assertions using Playwright's expect API

Playwright supports browser isolation, auto-waiting, and web-first assertions, which can be useful as this project grows into a larger automation framework. {"fallbackMarkdown":"(GitHub
)","reference":{"matched_text":"","prefix":null,"start_idx":5338,"end_idx":5357,"safe_urls":["https://github.com/microsoft/playwright/blob/main/README.md?plain=1","https://github.com/microsoft/playwright/blob/main/README.md?plain=1&utm_source=chatgpt.com"],"refs":[],"alt":"(GitHub
)","prompt_text":null,"type":"grouped_webpages","fallback_items":null,"items":[{"title":"playwright/README.md at main · microsoft/playwright · GitHub","url":"https://github.com/microsoft/playwright/blob/main/README.md?plain=1&utm_source=chatgpt.com","attribution":"GitHub","pub_date":null,"snippet":"","attribution_segments":null,"supporting_websites":[],"refs":[{"turn_index":0,"ref_type":"search","ref_index":7}],"hue":null,"attributions":null}],"status":"done","style":null,"error":null},"showLoginRequiredCard":false}

📚 Useful Resources
Playwright Documentation
Playwright Python API
The Internet - Login Page
👤 Author

malai777

GitHub: https://github.com/malai777

📄 License

This project is intended for learning and demonstration purposes.