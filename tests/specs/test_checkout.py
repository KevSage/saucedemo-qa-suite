import pytest
from playwright.sync_api import expect
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("username,should_succeed", [
    ("standard_user", True),
    ("problem_user", False),
])
def test_checkout_completion(authenticated_page, username, should_succeed):
    # test body here, using username and should_succeed
    page = authenticated_page(username)
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    page.get_by_test_id("shopping-cart-link").click()  # confirm this data-test value
    cart_page = CartPage(page)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_information("John", "Doe", "12345")
    if should_succeed:
      checkout_page.finish_checkout()
      expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html");
      expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    else:
      expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html");
      assert checkout_page.first_name_field.input_value() != "John"
      assert checkout_page.last_name_field.input_value() == "" 