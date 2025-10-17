"""
Test script to verify Playwright and Google Maps access
Run this to test if the scraper can access Google Maps
"""
import asyncio
from playwright.async_api import async_playwright


async def test_google_maps():
    print("Testing Google Maps access with Playwright...")
    
    async with async_playwright() as p:
        print("✓ Playwright initialized")
        
        # Launch browser (NOT headless so you can see what happens)
        browser = await p.chromium.launch(headless=False, timeout=60000)
        print("✓ Browser launched")
        
        # Create context
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        print("✓ Browser context created")
        
        # Create page
        page = await context.new_page()
        page.set_default_timeout(60000)
        print("✓ Page created")
        
        # Navigate to Google Maps
        print("Navigating to Google Maps...")
        try:
            await page.goto('https://www.google.com/maps', timeout=60000)
            print("✓ Successfully loaded Google Maps")
            
            # Wait a bit
            await asyncio.sleep(3)
            
            # Try to find search box
            try:
                search_box = page.locator('input#searchboxinput')
                await search_box.wait_for(state='visible', timeout=10000)
                print("✓ Search box found!")
                
                # Try to type
                await search_box.click()
                await search_box.fill("restaurants in New York")
                print("✓ Text entered successfully")
                
                # Take screenshot
                await page.screenshot(path='test_screenshot.png')
                print("✓ Screenshot saved as test_screenshot.png")
                
                print("\n✅ All tests passed! Google Maps is accessible.")
                
            except Exception as e:
                print(f"❌ Could not find search box: {e}")
                await page.screenshot(path='error_screenshot.png')
                print("  Screenshot saved as error_screenshot.png")
                
        except Exception as e:
            print(f"❌ Failed to load Google Maps: {e}")
        
        finally:
            # Keep browser open for 5 seconds so you can see it
            print("\nKeeping browser open for 5 seconds...")
            await asyncio.sleep(5)
            await browser.close()
            print("✓ Browser closed")


if __name__ == "__main__":
    asyncio.run(test_google_maps())
