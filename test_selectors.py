"""
Quick test script to debug Google Maps selectors
"""
import asyncio
from playwright.async_api import async_playwright


async def test_selectors():
    """Test different selectors on Google Maps search results"""
    
    async with async_playwright() as p:
        print("🚀 Launching browser...")
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to Google Maps
        print("📍 Navigating to Google Maps...")
        await page.goto('https://www.google.com/maps', wait_until='domcontentloaded')
        await asyncio.sleep(3)
        
        # Find search box
        print("🔍 Finding search box...")
        search_box = None
        selectors = [
            'input#searchboxinput',
            'input[name="q"]',
            'input[aria-label*="Search"]',
        ]
        
        for selector in selectors:
            try:
                search_box = page.locator(selector).first
                await search_box.wait_for(state='visible', timeout=5000)
                print(f"✅ Found search box with: {selector}")
                break
            except:
                continue
        
        if not search_box:
            print("❌ Could not find search box!")
            await browser.close()
            return
        
        # Type search query
        print("⌨️  Typing search query...")
        await search_box.click()
        await asyncio.sleep(0.5)
        await search_box.fill('')
        await search_box.type("restaurants in New York", delay=100)
        await asyncio.sleep(1)
        
        # Press Enter
        print("↩️  Pressing Enter...")
        await search_box.press('Enter')
        
        # Wait for results
        print("⏳ Waiting for results...")
        await asyncio.sleep(10)  # Give it plenty of time
        
        # Try different selectors
        print("\n🎯 Testing selectors:")
        print("-" * 50)
        
        test_selectors = [
            ('div[role="article"]', 'Business articles'),
            ('div[role="feed"]', 'Results feed'),
            ('a[href*="/maps/place/"]', 'Place links'),
            ('.hfpxzc', 'Card links'),
            ('.Nv2PK', 'Card containers'),
            ('div[jsaction*="mouseover"]', 'Interactive divs'),
        ]
        
        for selector, description in test_selectors:
            try:
                elements = page.locator(selector)
                count = await elements.count()
                print(f"{'✅' if count > 0 else '❌'} {description:20} ({selector}): {count} found")
                
                if count > 0 and count <= 3:
                    # Show first few elements' aria-labels
                    for i in range(min(count, 3)):
                        elem = elements.nth(i)
                        try:
                            aria_label = await elem.get_attribute('aria-label')
                            if aria_label:
                                print(f"   └─ [{i}] aria-label: {aria_label[:60]}...")
                        except:
                            pass
            except Exception as e:
                print(f"❌ {description:20} ({selector}): Error - {e}")
        
        print("\n" + "=" * 50)
        print("📄 Saving page HTML for inspection...")
        html = await page.content()
        with open('logs/test_page.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("✅ Saved to logs/test_page.html")
        
        print("\n📸 Taking screenshot...")
        await page.screenshot(path='logs/test_screenshot.png', full_page=True)
        print("✅ Saved to logs/test_screenshot.png")
        
        print("\n⏸️  Keeping browser open for manual inspection...")
        print("Press Ctrl+C to close")
        
        try:
            await asyncio.sleep(300)  # Keep open for 5 minutes
        except KeyboardInterrupt:
            print("\n👋 Closing...")
        
        await browser.close()


if __name__ == "__main__":
    asyncio.run(test_selectors())
