import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.regression
def test_add_single_item_to_cart(inventory_page: InventoryPage):
    product = "Sauce Labs Backpack"
    inventory_page.add_item_by_name(product)
    assert inventory_page.get_cart_count() == 1


@pytest.mark.regression
def test_full_checkout_flow(
        inventory_page: InventoryPage,
        cart_page: CartPage,
        checkout_page: CheckoutPage
):
    product = "Sauce Labs Fleece Jacket"

    # 1. Add to Cart & Open
    inventory_page.add_item_by_name(product)
    inventory_page.open_cart()

    # 2. Cart Verification
    cart_page.verify_product_in_cart(product)
    cart_page.proceed_to_checkout()

    # 3. Checkout Information & Completion
    checkout_page.fill_information("Jane", "Doe", "94016")
    checkout_page.finish_order()
    checkout_page.verify_order_completion()