import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def flask_server():
    """
    Fixture to start the Flask server before E2E tests and stop it after tests complete.
    """
    # Start Flask app
    flask_process = subprocess.Popen(['python', 'app.py'])
    # Wait for the server to start
    time.sleep(5)  # Adjust if your server takes longer to start
    yield
    # Terminate Flask server
    flask_process.terminate()
    flask_process.wait()

@pytest.fixture(scope="session")
def playwright_instance_fixture():
    """
    Fixture to manage Playwright's lifecycle.
    """
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance_fixture):
    browser = playwright_instance_fixture.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
