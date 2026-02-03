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

# --- TC-05: View Book Details from Shop Page ---
driver.get("https://sahup9156.github.io/bookworms/shop.html")
time.sleep(2)

# Click first book to view details
books = driver.find_elements(By.CSS_SELECTOR, ".product-men")
books[0].click()
time.sleep(2)

# Verify product details
try:
    details = driver.find_element(By.CSS_SELECTOR, ".col-md-8.single-right-left.simpleCart_shelfItem")
    title = details.find_element(By.TAG_NAME, "h3")
    price = details.find_element(By.TAG_NAME, "h6")
    print("TC-05 Passed: Book details page is displayed.")
    print("Book Title:", title.text)
    print("Book Price:", price.text)
except Exception as e:
    print("TC-05 Failed: Book details not found.")
    print("Error:", str(e))

driver.save_screenshot(os.path.join(screenshot_folder, "TC05_ViewBookDetails.png"))
driver.quit()