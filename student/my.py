from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://callback.58.com/antibot/verifycode?serialId=73e47afdafc8253d3edd71732301bb61_2ae2be5979634b75a696e0dd54c6647a&code=100&sign=dc3e2d6d5c48d9692b3ca76d3dccc887&namespace=zhaopin_list_pc&url=https%3A%2F%2Fsh.58.com%2Fjob%2Fpn2%2F%3Futm_source%3Dmarket%26spm%3Du-2d2yxv86y3v43nkddh1.BDPCPZ_BT%26key%3D%26pid%3D428659423751503872%26PGTID%3D0d302408-0000-23f0-15
    page.goto("https://callback.58.com/antibot/verifycode?serialId=73e47afdafc8253d3edd71732301bb61_2ae2be5979634b75a696e0dd54c6647a&code=100&sign=dc3e2d6d5c48d9692b3ca76d3dccc887&namespace=zhaopin_list_pc&url=https%3A%2F%2Fsh.58.com%2Fjob%2Fpn2%2F%3Futm_source%3Dmarket%26spm%3Du-2d2yxv86y3v43nkddh1.BDPCPZ_BT%26key%3D%26pid%3D428659423751503872%26PGTID%3D0d302408-0000-23f0-15")

    # Click text=点击按钮进行验证
    page.locator("text=点击按钮进行验证").click()

    # Click img
    page.locator("img").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
