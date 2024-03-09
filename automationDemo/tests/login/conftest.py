import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def set_up_tear_down() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({"width": 1536, "height": 800})
        page.goto("https://visas-fr.tlscontact.com/login")
        yield page
        browser.close()



