from playwright.sync_api import Page, Locator, expect
from tests.pages.base_page import BasePage

class CartPage(BasePage):
  def __init__(self, page: Page):
    super().__init__(page)
    self.checkout_button: Locator = page.get_by_test_id("checkout")

  def get_cart_item_names(self) -> list[str]:
      cart_items = self.page.get_by_test_id("inventory-item")  # find the right data-test for cart items
      names = []
      for item in cart_items.all():
          name = item.get_by_test_id("inventory-item-name").text_content()  # find the right data-test for item name within cart
          names.append(name)
      return names
  
  def go_to_checkout(self):
      self.checkout_button.click()
  
