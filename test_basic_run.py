from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page(no_viewport=True)
    page.goto("https://playwright.dev/")
    get_started_button = page.locator('[class="getStarted_Sjon"]')
    get_started_button.click()
    page.screenshot(path="screenshot.jpg")
    page.screenshot(path="full_screenshot.jpg", full_page=True)
    print(f'{page.title()=}')
    print(f'{page.url=}')

    expect(page).to_have_url("https://playwright.dev/docs/intro", timeout=20000)
    expect(page).to_have_title('Installation | Playwright')
    browser.close()