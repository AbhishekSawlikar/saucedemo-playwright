import os
from pathlib import Path
import pytest
from playwright.sync_api import Browser, Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

AUTH_DIR = Path(__file__).parent.parent / ".auth"
AUTH_FILE = AUTH_DIR / "user_state.json"


@pytest.fixture(scope="session")
def session_storage_state(browser: Browser):
    """Logs in once per test session and caches browser state."""
    AUTH_DIR.mkdir(parents=True, exist_ok=True)

    if not AUTH_FILE.exists():
        context = browser.new_context()
        page = context.new_page()

        login_p = LoginPage(page)
        login_p.navigate_to()
        login_p.login("standard_user", "secret_sauce")

        # Ensure login completed before dumping state
        page.wait_for_url("**/inventory.html")
        context.storage_state(path=str(AUTH_FILE))
        context.close()

    return str(AUTH_FILE)


@pytest.fixture(scope="function")
def authenticated_page(browser: Browser, session_storage_state: str) -> Page:
    """Provides a page pre-authenticated via the saved storage state."""
    context = browser.new_context(storage_state=session_storage_state)
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    yield page
    context.close()


# Page Object Fixtures
@pytest.fixture
def inventory_page(authenticated_page: Page) -> InventoryPage:
    return InventoryPage(authenticated_page)


@pytest.fixture
def cart_page(authenticated_page: Page) -> CartPage:
    return CartPage(authenticated_page)


@pytest.fixture
def checkout_page(authenticated_page: Page) -> CheckoutPage:
    return CheckoutPage(authenticated_page)