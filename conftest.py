import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def lunch(playwright: Playwright):
    chrome = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = chrome.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    chrome.close()
