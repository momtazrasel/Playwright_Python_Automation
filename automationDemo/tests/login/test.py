from playwright.sync_api import Page


def test_has_title(page: Page):
    page.goto("https://visas-fr.tlscontact.com/login")
