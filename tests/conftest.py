import pytest
from playwright.sync_api import Page, Playwright
from tests.pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def authenticated_page(page: Page):
    def _login_as(username: str, password: str = "secret_sauce") -> Page:
        page.goto("https://www.saucedemo.com/")
        login_page = LoginPage(page)
        login_page.login(username, password)
        return page

    yield _login_as