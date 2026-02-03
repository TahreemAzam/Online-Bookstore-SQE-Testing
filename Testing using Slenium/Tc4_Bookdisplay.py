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
#--C-04: Book Display on Shop Page ---
driver.get("Thttps://sahup9156.github.io/bookworms/shop.html")
time.sleep(3)

# Verify books/products are visible
products = driver.find_elements(By.CSS_SELECTOR, ".col-md-3.product-men")
if len(products) > 0:
    print("TC-04 Passed: Books are visible on the Shop page.")
else:
    print("TC-04 Failed: No books found on the Shop page.")

driver.save_screenshot(os.path.join(screenshot_folder, "TC04_BooksDisplay.png"))
driver.quit()