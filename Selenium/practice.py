from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or specify the path

# Navigate to a URL
driver.get("https://www.techwithtim.net/")  # Replace with your target URL

try:
    # Wait until the header element is present and clickable
    header = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "content__CardContentContainer-sc-1nrnigk-0"))
    )

    # Click the header element
    header.click()

    python = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "tag__TagContainer-sc-3f52y0-0"))
    )

    python.click()
    driver.back()
    driver.forward()
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Quit the driver
driver.quit()
