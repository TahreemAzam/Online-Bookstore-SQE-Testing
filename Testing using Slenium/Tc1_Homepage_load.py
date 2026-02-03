from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# --- Setup folder for screenshots ---
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# --- Setup Chrome Driver using webdriver-manager ---
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#TEST CASE 01: Homepage Loads

driver.get("https://sahup9156.github.io/bookworms/index.html")
time.sleep(2)  # wait for page to load

# Verify homepage title
expected_title = "BookWorms | Your One-Stop Shop for Personalized Book Recommendations and Online Purchases"
actual_title = driver.title

if expected_title in actual_title:
    print("TC-01 Passed: Homepage loaded successfully.")
else:
    print("TC-01 Failed: Homepage did not load.")

# Take screenshot
driver.save_screenshot(os.path.join(screenshot_folder, "TC01_Homepage.png"))
driver.quit()