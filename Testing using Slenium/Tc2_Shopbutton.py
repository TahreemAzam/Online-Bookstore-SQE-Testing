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
# --- TC-02: Shop Button Navigation from Homepage ---
driver.get("https://sahup9156.github.io/bookworms/index.html")
time.sleep(2)

# Click Shop button
try:
    shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
    shop_btn.click()
    time.sleep(2)

    # Verify shop page loaded by checking title
    if "Shop" in driver.title:
        print("TC-02 Passed: Shop button navigated to shop page.")
    else:
        print("TC-04 Failed: Shop page did not open.")
except Exception as e:
    print("TC-02 Failed:", str(e))

driver.save_screenshot(os.path.join(screenshot_folder, "TC02_ShopButton.png"))

driver.quit()