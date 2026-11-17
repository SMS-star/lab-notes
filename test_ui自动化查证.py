from playwright.sync_api import sync_playwright, expect  # 引入 expect

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    page.fill("input#kw", "Playwright 自动化测试")
    page.click("input#su")

    # 等待搜索页面的标题出现，并断言标题中包含我们搜索的词
    # Playwright 会自动等待，直到条件满足或者超时（默认30秒）
    try:
        expect(page).to_have_title("Playwright 自动化测试_百度搜索")
        print("✅ 断言成功：页面标题符合预期！")
    except Exception as e:
        print("❌ 断言失败：页面没加载出来或标题不对。")
    finally:
        page.wait_for_timeout(3000)  # 留3秒给你看结果
        browser.close()