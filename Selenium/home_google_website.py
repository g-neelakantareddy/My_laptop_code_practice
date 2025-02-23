from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to GitHub
driver.get("https://github.com/")

try:
    # Wait for the email input field to be present
    inputt = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user_email"))
    )

    # Send keys to the email input field
    inputt.send_keys("gneelakantareddy143@gmail.com")
    inputt.send_keys(Keys.RETURN)

    button = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains@(class,'js-hero-action')]"))
    )
    button.click()

    password = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    password.send_keys("143neela@")
    password.send_keys(Keys.RETURN)

except Exception as e:
    print(f"An error occurred: {e}")

# Wait for user input before closing the browser
input("Please enter to exit...")

# Quit the driver
driver.quit()
