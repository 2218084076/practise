from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://www.cdfgsanya.com/product-list.html?sw=%E8%B5%84%E7%94%9F%E5%A0%82
    page.goto("http://www.cdfgsanya.com/product-list.html?sw=%E8%B5%84%E7%94%9F%E5%A0%82")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
