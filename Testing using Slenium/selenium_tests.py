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

# --- TC-01: Shop Page Load & Book Display ---
driver.get("https://sahup9156.github.io/bookworms/shop.html")
time.sleep(2)

books = driver.find_elements(By.CSS_SELECTOR, ".product-men")
if len(books) > 0:
    print("TC-01 Passed: Shop page loaded and books visible.")
else:
    print("TC-01 Failed: No books found.")

driver.save_screenshot(os.path.join(screenshot_folder, "TC01_ShopPage.png"))

# --- TC-02: Open Product Details Page ---
books[0].click()
time.sleep(2)

try:
    title = driver.find_element(By.CSS_SELECTOR, ".col-md-8.single-right-left.simpleCart_shelfItem")
    price = driver.find_element(By.CLASS_NAME, "caption")
    print("TC-02 Passed: Product details page opened successfully.")
except:
    print("TC-02 Failed: Product details not found.")

driver.save_screenshot(os.path.join(screenshot_folder, "TC02_ProductDetails.png"))
driver.back()
time.sleep(1)

# --- TC-03: Add Book to Cart & View Cart ---
add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, ".chr-cart.pchr-cart")
add_to_cart_btn.click()
time.sleep(1)

cart_link = driver.find_element(By.CSS_SELECTOR, ".top_chr_cart")
cart_link.click()
time.sleep(2)

#cart_items = driver.find_elements(By.CLASS_NAME, ".simpleCart_items .item")
if "checkout" in driver.current_url:
    print("TC-03 Passed: Cart page opened successfully.")
else:
    print("TC-03 Failed: Cart page did not open.")

driver.save_screenshot(os.path.join(screenshot_folder, "TC03_Cart.png"))

driver.quit()
