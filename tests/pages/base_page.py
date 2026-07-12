from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def wait_for_element(self, locator: Locator, timeout: int = 10000):
        locator.wait_for(state="visible", timeout=timeout)