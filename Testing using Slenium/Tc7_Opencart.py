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
# --- TC-07: Cart Page Access from Shop Page ---
driver.get("https://sahup9156.github.io/bookworms/shop.html")
time.sleep(2)

# Click Cart link from navbar
try:
    cart_link = driver.find_element(By.CSS_SELECTOR, ".top_chr_cart")
    cart_link.click()
    time.sleep(2)
    print("TC-07 Passed: Cart page opened.")
except Exception as e:
    print("TC-07 Failed: Could not open cart.", str(e))

driver.save_screenshot(os.path.join(screenshot_folder, "TC07_CartPage.png"))
driver.quit()