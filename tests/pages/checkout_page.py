from playwright.sync_api import Page, Locator
from tests.pages.base_page import BasePage

class CheckoutPage(BasePage):
  def __init__(self, page: Page):
    super().__init__(page)
    self.first_name_field: Locator = page.get_by_test_id("firstName")
    self.last_name_field: Locator = page.get_by_test_id("lastName")
    self.postal_code_field: Locator = page.get_by_test_id("postalCode")
    self.continue_button: Locator = page.get_by_test_id("continue")


  def checkout(self, first_name: str, last_name: str, postal_code: str):
    self.first_name_field.type(first_name)
    self.last_name_field.type(last_name)
    self.postal_code_field.type(postal_code)
    self.continue_button.click()
