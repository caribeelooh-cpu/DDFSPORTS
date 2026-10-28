async def run_test(page, output_dir, page_url):
    import re
    try:
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(1500)
        title = await page.title()
        metas = await page.locator('head meta[name="google-site-verification"]').count()
        html = await page.locator('head').inner_html()
        print(f"TITLE={title}")
        print(f"PUBLIC_META_COUNT={metas}")
        print(f"PUBLIC_PLACEHOLDER={'%REACT_APP_GOOGLE_SITE_VERIFICATION_TOKEN%' in html}")
        login_text = await page.get_by_text(re.compile("login|entrar|sign in", re.I)).count()
        print(f"LOGIN_TEXT_COUNT={login_text}")
        error_text = await page.evaluate("""() => { const errorElements = Array.from(document.querySelectorAll('.error, [class*="error"], [id*="error"]')); return errorElements.map(el => el.textContent).join(', '); }""")
        print(f"ERROR_TEXT={error_text}")
        print("PUBLIC_UI_PASS" if title and metas == 1 and '%REACT_APP_GOOGLE_SITE_VERIFICATION_TOKEN%' not in html else "PUBLIC_UI_FINDING")
    except Exception as e:
        print(f"FINDING: {e}")
