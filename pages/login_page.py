from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_container = page.locator('[data-test="error"]')

    def login(self, username: str = "standard_user", password: str = "secret_sauce"):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_error_displayed(self, expected_message: str):
        expect(self.error_container).to_contain_text(expected_message)