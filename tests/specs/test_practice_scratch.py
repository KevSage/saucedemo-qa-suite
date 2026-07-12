from playwright.sync_api import expect
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage

def test_can_add_and_remove_items_from_cart(authenticated_page):
  page = authenticated_page("standard_user")
  inventory_page = InventoryPage(page)
  # card = inventory_page.get_product_card("Sauce Labs Backpack")
  # expect(card).to_be_visible

  initial_count = inventory_page.get_cart_badge_count()
  assert initial_count == 0

  #Add Item to cart
  inventory_page.add_to_cart("Sauce Labs Backpack")
  updated_count = inventory_page.get_cart_badge_count()
  assert updated_count == 1

  #Remove item from cart
  inventory_page.remove_from_cart("Sauce Labs Backpack")
  updated_count = inventory_page.get_cart_badge_count()
  assert updated_count == 0

def test_debug_product_details(authenticated_page):
    page = authenticated_page("standard_user")


    inventory_page = InventoryPage(page)
    card = inventory_page.get_product_card("Sauce Labs Backpack")
    details = inventory_page.get_product_details(card)
    print(details)

def test_debug_cart_item_names(authenticated_page):
    page = authenticated_page("standard_user")
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("Sauce Labs Backpack")

    page.get_by_test_id("shopping-cart-link").click()  # confirm this data-test value in DevTools

    cart_page = CartPage(page)
    names = cart_page.get_cart_item_names()
    print(names)    

def test_debug_problem_user_checkout_bug(authenticated_page):
    page = authenticated_page("problem_user")
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("Sauce Labs Backpack")

    page.get_by_test_id("shopping-cart-link").click()  # confirm this data-test value
    cart_page = CartPage(page)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.checkout("John", "Doe", "12345")

    print(f"First name field value: {checkout_page.first_name_field.input_value()}")
    print(f"Last name field value: {checkout_page.last_name_field.input_value()}")