from playwright.sync_api import Page, Locator
from tests.pages.base_page import BasePage

class LoginPage(BasePage):
  def __init__(self, page: Page):
    super().__init__(page)
    self.username_field: Locator = page.get_by_test_id("username")
    self.password_field: Locator = page.get_by_test_id("password")
    self.login_button: Locator = page.get_by_test_id("login-button")
    self.error_message: Locator = page.get_by_test_id("error")

  def login(self, username: str, password: str):
    self.username_field.fill(username)
    self.password_field.fill(password)
    self.login_button.click()

  def get_error_message(self) -> str | None:
    return self.error_message.text_content()