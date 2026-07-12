from playwright.sync_api import Page, Locator, expect
from tests.pages.base_page import BasePage
from tests.test_data.products import EXPECTED_PRODUCTS

class InventoryPage(BasePage):
  def __init__(self, page: Page):
    super().__init__(page)
    self.inventory_items = page.get_by_test_id("inventory-item") 
  
  def get_product_card(self, product_name: str) -> Locator:
    return self.inventory_items.filter(has_text=product_name)
  
  def add_to_cart(self, product_name: str):
    product_card = self.get_product_card(product_name)
    button = product_card.get_by_role("button", name="Add to cart")
    button.click()

  def remove_from_cart(self, product_name: str):
    product_card = self.get_product_card(product_name)
    button = product_card.get_by_role("button", name="Remove")
    button.click()

  def get_cart_badge_count(self) -> int:
    badge= self.page.get_by_test_id("shopping-cart-badge")
    if badge.count() == 0:
      return 0
    return int(badge.text_content())
