"""
Test script for cross-platform notifications
Run this to verify notifications are working on your system
"""
import time
from src.utils.notifier import Notifier

def test_notifications():
    """Test all notification types"""
    
    print("Testing Desktop Notifications...")
    print("-" * 50)
    
    # Test 1: Info notification
    print("\n1. Testing INFO notification...")
    Notifier.notify_info("This is an info notification")
    time.sleep(2)
    
    # Test 2: Success notification
    print("2. Testing SUCCESS notification...")
    Notifier.notify_success("Operation completed successfully!")
    time.sleep(2)
    
    # Test 3: Warning notification
    print("3. Testing WARNING notification...")
    Notifier.notify_warning("This is a warning message")
    time.sleep(2)
    
    # Test 4: Error notification
    print("4. Testing ERROR notification...")
    Notifier.notify_error("An error has occurred")
    time.sleep(2)
    
    # Test 5: Completion notification
    print("5. Testing COMPLETION notification...")
    Notifier.notify_complete(total_results=150, total_tasks=5)
    time.sleep(2)
    
    # Test 6: Custom notification
    print("6. Testing CUSTOM notification...")
    Notifier.notify(
        title="🗺️ Google Maps Scraper",
        message="Custom notification with 15 second timeout",
        timeout=15
    )
    
    print("\n" + "-" * 50)
    print("✅ All notification tests completed!")
    print("You should have seen 6 desktop notifications.")
    print("\nNote: If you didn't see notifications:")
    print("1. Make sure plyer is installed: pip install plyer")
    print("2. Check your system notification settings")
    print("3. On Windows, ensure notifications are enabled in Settings > System > Notifications")

if __name__ == "__main__":
    test_notifications()
