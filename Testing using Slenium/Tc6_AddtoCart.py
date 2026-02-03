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

# --- TC-06: Add to Cart Functionality on Shop Page ---
driver.get("https://sahup9156.github.io/bookworms/shop.html")
time.sleep(2)

# Click Add to Cart button
try:
    add_btn = driver.find_element(By.CSS_SELECTOR, ".chr-cart.pchr-cart")
    add_btn.click()
    time.sleep(1)
    print("TC-06 Passed: Product added to cart.")
except Exception as e:
    print("TC-06 Failed: Could not click Add to Cart.", str(e))

driver.save_screenshot(os.path.join(screenshot_folder, "TC06_AddToCart.png"))
driver.quit()