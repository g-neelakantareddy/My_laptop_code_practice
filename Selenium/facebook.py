from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging
import os
import pickle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

driver = webdriver.Chrome()
logging.info("Chrome launched")

driver.maximize_window()

driver.get("https://www.facebook.com/")

if os.path.exists('cookies.pkl', 'rb'):
    with open('cookies.pkl') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()



email_phone = WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#email"))
)
with open('details.txt', 'r') as file:
    phone_number = file.readline().strip()
email_phone.send_keys(phone_number)
logging.info("email or phone number added")

driver.save_screenshot('error.png')
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='pass']"))
)
password.send_keys("@neela143")

driver.find_element(By.CSS_SELECTOR,"button[name='login']").click()

input("waitsss...")

driver.quit()