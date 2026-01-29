#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

# ============================================
# CONFIGURATION
# ============================================
TARGET_URL = "https://lcnjoel.com/mulon/casino/crash.html"

# Firefox profile path - UPDATE THIS!
# Run: find ~/.mozilla/firefox -name "*.default*" -type d
FIREFOX_PROFILE_PATH = "/home/piano/.mozilla/firefox/riwlp3yd.default-release"

# Loop settings
CLICKS_PER_CYCLE = 100           # Number of skip button clicks before restarting
WAIT_BETWEEN_CLICKS = 0.7        # Seconds between skip clicks (adjust for speed)
MAX_RETRIES = 7                  # Max retries if buttons not found

# ============================================
# FIREFOX SETUP WITH PROFILE
# ============================================
print("Setting up Firefox with infinite click loop...")

# Firefox options
firefox_options = Options()

# Use existing profile if available
if os.path.exists(FIREFOX_PROFILE_PATH):
    print(f"✓ Using Firefox profile: {FIREFOX_PROFILE_PATH}")
    firefox_options.add_argument(f'-profile')
    firefox_options.add_argument(FIREFOX_PROFILE_PATH)
else:
    print(f"⚠️ Profile not found, creating new session")
    # List available profiles
    try:
        profiles_dir = "/home/piano/.mozilla/firefox"
        if os.path.exists(profiles_dir):
            for item in os.listdir(profiles_dir):
                item_path = os.path.join(profiles_dir, item)
                if os.path.isdir(item_path) and ("default" in item):
                    FIREFOX_PROFILE_PATH = item_path
                    firefox_options.add_argument(f'-profile')
                    firefox_options.add_argument(FIREFOX_PROFILE_PATH)
                    print(f"Using found profile: {FIREFOX_PROFILE_PATH}")
                    break
    except:
        pass

# Firefox preferences
firefox_options.set_preference("dom.webdriver.enabled", False)
firefox_options.set_preference("useAutomationExtension", False)
firefox_options.set_preference("browser.tabs.warnOnClose", False)
firefox_options.set_preference("browser.startup.homepage", "about:blank")
firefox_options.set_preference("browser.safebrowsing.enabled", False)

# ============================================
# HELPER FUNCTIONS
# ============================================
def find_and_click(driver, selectors, timeout=10, element_name="element"):
    """Find and click an element using multiple selectors"""
    for by, selector in selectors:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            # Check if it's visible (for skip button with display: block)
            style = element.get_attribute("style")
            if "skip" in element_name.lower() and style and "display: none" in style:
                continue
            
            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.1)
            
            # Try to click
            try:
                element.click()
            except:
                driver.execute_script("arguments[0].click();", element)
            
            print(f"✓ {element_name} clicked: {by}='{selector}'")
            return True
        except:
            continue
    return False

def click_start_auto(driver, retries=MAX_RETRIES):
    """Click the Start Auto button with retries"""
    start_selectors = [
        (By.ID, "autoStartBtn"),
        (By.CSS_SELECTOR, "#autoStartBtn"),
        (By.CSS_SELECTOR, ".bet-btn"),
        (By.XPATH, "//button[contains(@class, 'bet-btn')]"),
        (By.XPATH, "//button[contains(text(), 'Start')]"),
        (By.XPATH, "//button[contains(text(), 'Auto')]"),
    ]
    
    for attempt in range(retries):
        print(f"Attempt {attempt + 1}/{retries} to click Start Auto...")
        if find_and_click(driver, start_selectors, timeout=5, element_name="Start Auto"):
            return True
        time.sleep(1)
    
    print("❌ Failed to click Start Auto button")
    return False

def click_skip_button(driver, retries=MAX_RETRIES):
    """Click the Skip button with retries"""
    skip_selectors = [
        (By.ID, "skipBtn"),
        (By.CSS_SELECTOR, "#skipBtn"),
        (By.CSS_SELECTOR, ".skip-btn"),
        (By.XPATH, "//button[contains(@class, 'skip-btn')]"),
        (By.XPATH, "//button[contains(text(), 'Skip')]"),
        (By.XPATH, "//button[@style='display: block']"),
        (By.XPATH, "//button[contains(@style, 'display: block')]"),
    ]
    
    for attempt in range(retries):
        if find_and_click(driver, skip_selectors, timeout=2, element_name="Skip"):
            return True
        time.sleep(0.5)
    
    return False

# ============================================
# MAIN AUTOMATION LOOP
# ============================================
def main_automation_loop():
    """Main loop that runs forever"""
    
    # Setup Firefox
    try:
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        print("✓ Firefox started successfully!")
    except Exception as e:
        print(f"❌ Failed to start Firefox: {e}")
        return
    
    try:
        # Navigate to target page
        print(f"\n🌐 Navigating to: {TARGET_URL}")
        driver.get(TARGET_URL)
        time.sleep(5)
        
        # Login checkpoint
        # Login checkpoint
        print("\n" + "="*50)
        print("LOGIN CHECKPOINT")
        print("="*50)
        print("Please sign in with Google if needed.")
        print("After logging in, press ENTER here to continue...")
        input()  # Wait for user to press Enter
        print("Starting automation loop...")
        
        cycle_count = 0
        
        # INFINITE LOOP
        while True:
            cycle_count += 1
            print(f"\n{'='*60}")
            print(f"CYCLE {cycle_count} STARTED")
            print(f"{'='*60}")
            
            # STEP 1: Click Start Auto
            if not click_start_auto(driver):
                print("⚠️ Could not start cycle, refreshing page...")
                driver.refresh()
                time.sleep(5)
                continue
            
            time.sleep(2)  # Wait for game to start
            
            # STEP 2: Click Skip button 100 times
            skip_clicks = 0
            consecutive_fails = 0
            max_consecutive_fails = 5
            
            print(f"\nStarting {CLICKS_PER_CYCLE} skip clicks...")
            
            while skip_clicks < CLICKS_PER_CYCLE:
                # Try to click skip button
                if click_skip_button(driver):
                    skip_clicks += 1
                    consecutive_fails = 0
                    
                    # Progress indicator
                    if skip_clicks % 10 == 0:
                        print(f"  Skip clicks: {skip_clicks}/{CLICKS_PER_CYCLE}")
                    
                    # Wait between clicks
                    time.sleep(WAIT_BETWEEN_CLICKS)
                else:
                    consecutive_fails += 1
                    print(f"  Missed skip click #{skip_clicks + 1} (fail {consecutive_fails}/{max_consecutive_fails})")
                    
                    if consecutive_fails >= max_consecutive_fails:
                        print("  Too many consecutive fails, breaking...")
                        break
                    
                    time.sleep(1)
            
            print(f"\n✓ Cycle {cycle_count} complete: {skip_clicks} skip clicks")
            
            # Statistics
            total_time = cycle_count * (CLICKS_PER_CYCLE * WAIT_BETWEEN_CLICKS + 5)
            hours = total_time // 3600
            minutes = (total_time % 3600) // 60
            seconds = total_time % 60
            
            print(f"Total runtime: {hours}h {minutes}m {seconds}s")
            print(f"Total cycles: {cycle_count}")
            print(f"Total skip clicks: {cycle_count * CLICKS_PER_CYCLE}")
            
            # Check if page is still responsive
            try:
                current_url = driver.current_url
                if TARGET_URL not in current_url:
                    print("⚠️ Page changed, reloading...")
                    driver.get(TARGET_URL)
                    time.sleep(5)
            except:
                print("⚠️ Page not responding, reloading...")
                driver.get(TARGET_URL)
                time.sleep(5)
            
            # Small delay before next cycle
            print("Waiting 2 seconds before next cycle...")
            time.sleep(2)
    
    except KeyboardInterrupt:
        print("\n\n🛑 Script stopped by user (Ctrl+C)")
    
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cleanup
        print("\n" + "="*60)
        print("CLEANING UP...")
        print("="*60)
        
        try:
            driver.quit()
            print("✓ Firefox closed")
        except:
            pass
        
        print("\n✨ Automation finished")

# ============================================
# START THE LOOP
# ============================================
if __name__ == "__main__":
    print("="*60)
    print("INFINITE FIREFOX AUTOMATION")
    print("="*60)
    print(f"Target URL: {TARGET_URL}")
    print(f"Skip clicks per cycle: {CLICKS_PER_CYCLE}")
    print(f"Wait between clicks: {WAIT_BETWEEN_CLICKS} seconds")
    print(f"Running FOREVER until Ctrl+C is pressed")
    print("\n" + "="*60)
    
    # Instructions
    print("\nINSTRUCTIONS:")
    print("1. Make sure Firefox profile path is correct")
    print("2. The script will pause for 15 seconds for login")
    print("3. Press Ctrl+C in terminal to stop")
    print("="*60 + "\n")
    
    # Wait for user confirmation
    input("Press ENTER to start (or Ctrl+C to cancel)...")
    
    # Run the main loop
    main_automation_loop()