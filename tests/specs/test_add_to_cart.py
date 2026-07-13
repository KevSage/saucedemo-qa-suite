from tests.pages.inventory_page import InventoryPage


def test_standard_user_can_add_item_to_cart(authenticated_page):
    page = authenticated_page("standard_user")
    inventory_page = InventoryPage(page)

    initial_count = inventory_page.get_cart_badge_count()
    assert initial_count == 0

    inventory_page.add_to_cart("Sauce Labs Backpack")

    updated_count = inventory_page.get_cart_badge_count()
    assert updated_count == 1