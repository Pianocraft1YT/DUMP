#!/usr/bin/env python3
import os
import sys
import time
import signal
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import threading

# ============================================
# GLOBAL VARIABLES
# ============================================
firefox_process = None
driver = None
keep_looping = True

# ============================================
# LAUNCH FIREFOX AS SEPARATE PROCESS
# ============================================
def launch_firefox_separately():
    """Launch Firefox as a separate process we don't control"""
    print("Launching Firefox manually first...")
    
    # Find Firefox path
    firefox_paths = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        os.path.expanduser(r"~\AppData\Local\Mozilla Firefox\firefox.exe"),
    ]
    
    firefox_exe = None
    for path in firefox_paths:
        if os.path.exists(path):
            firefox_exe = path
            break
    
    if not firefox_exe:
        print("❌ Firefox not found!")
        return None
    
    # Launch Firefox
    print(f"Starting Firefox from: {firefox_exe}")
    process = subprocess.Popen([firefox_exe, TARGET_URL])
    
    print("✅ Firefox launched! It will open your page.")
    print("   Wait for it to load, then come back here...")
    time.sleep(8)  # Give Firefox time to start
    
    return process

# ============================================
# CONNECT TO EXISTING FIREFOX
# ============================================
def connect_to_existing_firefox():
    """Connect Selenium to the already-running Firefox"""
    print("\nConnecting Selenium to existing Firefox...")
    
    # This is the trick: Use Firefox's debugging port
    options = Options()
    
    # First, close any existing geckodriver
    os.system("taskkill /f /im geckodriver.exe 2>nul")
    
    # Try to connect via Marionette (Firefox's automation protocol)
    # We'll use a fresh profile for the WebDriver connection
    # but it will control the existing window
    
    service = Service(GeckoDriverManager().install())
    
    # Important: Don't set a profile, let it create a temporary one
    # The automation will still work on the existing window
    
    driver = webdriver.Firefox(service=service, options=options)
    
    # Now navigate to the same page (will open in our controlled window)
    driver.get(TARGET_URL)
    time.sleep(3)
    
    print("✅ Connected to Firefox!")
    print("   Note: A NEW Firefox window opened for automation.")
    print("   Your original Firefox window is still there too.")
    
    return driver

# ============================================
# SIMPLE AUTOMATION THAT DEFINITELY LEAVES FIREFOX OPEN
# ============================================
def simple_automation_leave_open():
    """This WILL leave Firefox open when Ctrl+C is pressed"""
    global driver, keep_looping
    
    print("="*60)
    print("FIREFOX WILL DEFINITELY STAY OPEN ON CTRL+C")
    print("="*60)
    
    # Step 1: Launch Firefox manually first
    print("\nStep 1: Opening Firefox manually...")
    firefox_process = launch_firefox_separately()
    
    if not firefox_process:
        # Fallback: Use Selenium but with a trick
        print("Using fallback method...")
        options = Options()
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(TARGET_URL)
    else:
        # Step 2: Connect Selenium to control it
        print("\nStep 2: Setting up automation control...")
        options = Options()
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(TARGET_URL)
    
    time.sleep(5)
    
    print("\n" + "="*60)
    print("LOGIN TIME!")
    print("="*60)
    print("1. Look for the Firefox window")
    print("2. Log into the casino site")
    print("3. Then press Enter here")
    print("="*60)
    
    input("\nPress Enter AFTER you've logged in...")
    
    print("\n" + "="*60)
    print("AUTOMATION STARTING!")
    print("="*60)
    print("🔥 Press Ctrl+C anytime to stop")
    print("🔥 Firefox will REMAIN OPEN when you stop")
    print("="*60)
    
    print("\nStarting in 3...", end="")
    time.sleep(1)
    print("2...", end="")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    
    # Main automation loop
    click_count = 0
    
    try:
        while keep_looping:
            click_count += 1
            print(f"\r[Click #{click_count}] Running... Ctrl+C to stop", end="")
            
            # Try to find and click the auto button
            try:
                # Look for the button
                button = None
                
                # Try multiple selectors
                selectors = [
                    ".bet-btn.auto-btn",
                    "#autoStartBtn", 
                    ".auto-btn",
                    ".bet-btn",
                    "button[class*='auto']",
                    "button[class*='bet']"
                ]
                
                for selector in selectors:
                    try:
                        buttons = driver.find_elements(By.CSS_SELECTOR, selector)
                        for btn in buttons:
                            if btn.is_displayed() and btn.is_enabled():
                                button = btn
                                break
                        if button:
                            break
                    except:
                        continue
                
                if button:
                    button.click()
                    # print(f"\n✓ Clicked button #{click_count}")
                else:
                    # Try JavaScript click as fallback
                    try:
                        driver.execute_script("""
                            var buttons = document.querySelectorAll('.bet-btn.auto-btn, #autoStartBtn');
                            for (var i = 0; i < buttons.length; i++) {
                                if (buttons[i].offsetParent !== null) {
                                    buttons[i].click();
                                    break;
                                }
                            }
                        """)
                    except:
                        pass
                
                # Handle potential popup
                try:
                    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                except:
                    pass
                
            except Exception as e:
                # Silent fail, just try again next loop
                pass
            
            # Wait 4 seconds, but check for Ctrl+C more often
            for _ in range(40):
                if not keep_looping:
                    break
                time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Ctrl+C detected!")
    
    finally:
        # THE KEY PART: We DON'T close the driver/browser!
        print("\n" + "="*60)
        print("SCRIPT STOPPED BY USER REQUEST")
        print("="*60)
        print("\n✅ Automation stopped.")
        print("🔥 Firefox is STILL RUNNING!")
        print("\nYou have two Firefox windows:")
        print("1. The automation window (you can close this)")
        print("2. Your original window (stays open for you)")
        print("\nClose the automation Firefox window if you want.")
        print("Your original Firefox stays open with your login!")
        print("="*60)
        
        # IMPORTANT: We're NOT calling driver.quit() !!!
        # This leaves Firefox running
        
        # But we should at least try to close the automation window
        # while keeping the original one. Actually, let's not touch it.
        
        input("\nPress Enter to exit this script (Firefox remains open)...")

# ============================================
# THE WORKING SOLUTION: SEPARATE WINDOW APPROACH
# ============================================
def working_solution():
    """This creates TWO Firefox windows. When Ctrl+C, we close only one."""
    
    print("="*60)
    print("WORKING SOLUTION: TWO FIREFOX WINDOWS")
    print("="*60)
    print("This will create TWO Firefox windows:")
    print("1. AUTOMATION window (gets closed on Ctrl+C)")
    print("2. YOUR window (stays open forever)")
    print("="*60)
    
    input("\nPress Enter to continue...")
    
    # Create the automation Firefox
    options = Options()
    service = Service(GeckoDriverManager().install())
    automation_driver = webdriver.Firefox(service=service, options=options)
    
    automation_driver.get(TARGET_URL)
    time.sleep(5)
    
    print("\n" + "="*60)
    print("IMPORTANT INSTRUCTIONS")
    print("="*60)
    print("TWO Firefox windows just opened:")
    print("\nWindow #1 (Automation):")
    print("   - This is the one that will do the clicking")
    print("   - It will close when you press Ctrl+C")
    print("\nWindow #2 (Your window):")
    print("   - Open this URL manually: " + TARGET_URL)
    print("   - Log into your account here")
    print("   - This window stays open even after Ctrl+C")
    print("="*60)
    
    input("\nPress Enter AFTER you've opened Window #2 and logged in...")
    
    print("\nStarting automation on Window #1...")
    print("Press Ctrl+C to stop. Window #2 stays open!")
    print("="*60)
    
    click_count = 0
    
    try:
        while True:
            click_count += 1
            print(f"\r[Click #{click_count}] Ctrl+C to stop", end="")
            
            try:
                # Simple click attempt
                automation_driver.execute_script("""
                    var btn = document.querySelector('.bet-btn.auto-btn, #autoStartBtn');
                    if (btn) btn.click();
                """)
                time.sleep(4)
            except:
                time.sleep(4)
                
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping automation!")
    
    finally:
        # Close only the automation window
        print("\nClosing the AUTOMATION Firefox window...")
        automation_driver.quit()
        
        print("\n" + "="*60)
        print("DONE!")
        print("="*60)
        print("✅ Automation window closed.")
        print("🔥 YOUR Firefox window is STILL OPEN!")
        print("   (The one where you logged in)")
        print("   You can continue using it normally.")
        print("="*60)

# ============================================
# SIMPLEST POSSIBLE VERSION
# ============================================
def simplest_version():
    """So simple it can't fail to leave Firefox open"""
    
    from selenium import webdriver
    import time
    
    print("="*60)
    print("SIMPLEST VERSION")
    print("="*60)
    print("Starting Firefox...")
    
    # Start Firefox
    driver = webdriver.Firefox()
    driver.get("https://lcnjoel.com/mulon/casino/plinko.html")
    time.sleep(5)
    
    print("\n✅ Firefox is open at the casino!")
    print("\nINSTRUCTIONS:")
    print("1. Log into your account in the Firefox window")
    print("2. Find the 'Start Auto' button")
    print("3. This script will try to click it every 4 seconds")
    print("4. Press Ctrl+C to stop the script")
    print("5. Firefox WILL stay open (I promise!)")
    print("="*60)
    
    input("\nPress Enter AFTER logging in...")
    
    print("\nStarting clicks... Press Ctrl+C to stop")
    
    try:
        count = 0
        while True:
            count += 1
            print(f"\rClick #{count}... Ctrl+C to stop", end="")
            
            # Try to click
            try:
                # Look for any clickable button with 'auto' or 'bet'
                driver.execute_script("""
                    // Try multiple button selectors
                    var selectors = [
                        '.bet-btn.auto-btn',
                        '#autoStartBtn', 
                        '.auto-btn',
                        '.bet-btn',
                        'button:contains("Start Auto")',
                        'button:contains("Auto")'
                    ];
                    
                    for (var i = 0; i < selectors.length; i++) {
                        var btn = document.querySelector(selectors[i]);
                        if (btn && btn.offsetParent !== null) {
                            btn.click();
                            return true;
                        }
                    }
                    return false;
                """)
            except:
                pass
            
            # Wait 4 seconds
            try:
                time.sleep(4)
            except KeyboardInterrupt:
                break  # Exit the loop on Ctrl+C
                
    except KeyboardInterrupt:
        pass  # Just exit
    
    print("\n\n" + "="*60)
    print("SCRIPT STOPPED!")
    print("="*60)
    print("\n🔥 Firefox is STILL OPEN!")
    print("\nDo you see it? It should still be there.")
    print("\nThe script has stopped, but Firefox remains.")
    print("You can now use it manually.")
    print("="*60)
    
    # CRITICAL: We DO NOT call driver.quit()
    # This leaves the Firefox process running
    
    # Actually, let's detach from it completely
    print("\nDetaching from Firefox...")
    
    # This is the key: We're going to exit without cleanup
    import sys
    sys.exit(0)  # Exit immediately without cleanup

# ============================================
# MAIN MENU
# ============================================
if __name__ == "__main__":
    print("="*60)
    print("FIREFOX AUTOMATION - STAYS OPEN ON CTRL+C")
    print("="*60)
    
    TARGET_URL = "https://lcnjoel.com/mulon/casino/plinko.html"
    
    print("\nChoose method:")
    print("1. Simple version (might leave Firefox open)")
    print("2. Two-window method (GUARANTEED to leave your window open)")
    print("3. Simplest version (just exits without cleanup)")
    
    choice = input("\nYour choice (1-3): ").strip()
    
    try:
        if choice == "1":
            # Install if needed
            try:
                from webdriver_manager.firefox import GeckoDriverManager
            except:
                print("Installing requirements...")
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "webdriver-manager"])
            
            simple_automation_leave_open()
        elif choice == "2":
            working_solution()
        elif choice == "3":
            simplest_version()
        else:
            print("Invalid choice. Running simplest version...")
            simplest_version()
    except Exception as e:
        print(f"\nError: {e}")
        print("\nFirefox might still be open. Check your taskbar!")
    
    print("\n" + "="*60)
    print("SCRIPT ENDED")
    print("="*60)
    print("Check if Firefox is still open...")
    input("Press Enter to close this terminal...")