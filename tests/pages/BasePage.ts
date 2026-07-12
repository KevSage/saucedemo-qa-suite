import { Page, Locator } from "@playwright/test";

export class BasePage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async navigateTo(url: string) {
    await this.page.goto(url);
  }
  async waitForElement(locator: Locator, timeout: number = 10000) {
    await locator.waitFor({ state: "visible", timeout });
  }
}
