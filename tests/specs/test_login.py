from tests.pages.login_page import LoginPage

def test_locked_out_user_cannot_login(page):
  page.goto("https://www.saucedemo.com/")
  login_page = LoginPage(page)
  login_page.login("locked_out_user", "secret_sauce")

  error_message = login_page.get_error_message().lower()
  assert page.url == "https://www.saucedemo.com/"