from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, path: str = ""):
        self.page.goto(f"https://www.saucedemo.com/{path.lstrip('/')}")

    def verify_url_contains(self, segment: str):
        expect(self.page).to_have_url(lambda url: segment in url)