from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Step 1: Customer details
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')

        # Step 2: Overview & Summary
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('.complete-header')

    def fill_information(self, first: str, last: str, zip_code: str):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.postal_code_input.fill(zip_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def verify_order_completion(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")