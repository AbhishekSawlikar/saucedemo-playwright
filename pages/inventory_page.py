from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_header = page.locator('.title')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.cart_link = page.locator('.shopping_cart_link')
        self.inventory_items = page.locator('.inventory_item')

    def add_item_by_name(self, product_name: str):
        item_card = self.inventory_items.filter(has_text=product_name)
        item_card.locator('button[data-test^="add-to-cart"]').click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def open_cart(self):
        self.cart_link.click()