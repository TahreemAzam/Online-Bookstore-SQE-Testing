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
# --- TC-03: Logo Visibility on Homepage ---
driver.get("https://sahup9156.github.io/bookworms/index.html")
time.sleep(2)

# Verify logo is visible
try:
    logo = driver.find_element(By.CLASS_NAME, "logo")
    print("TC-03 Passed: Logo is visible.")
except:
    print("TC-03 Failed: Logo not found.")

driver.save_screenshot(os.path.join(screenshot_folder, "TC03_Logo.png"))

driver.quit()