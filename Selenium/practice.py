from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

firefox_options = webdriver.ChromeOptions()

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.XPATH, "//div[normalize-space()='Courses']")

# create action chain object
action = ActionChains(driver)

# perform the operation
action.context_click(element).click()
action.perform()
sleep(3)

sleep(1)
pyautogui.press('down')   # Navigate down in the menu
sleep(0.5)
pyautogui.press('down')   # Navigate again
sleep(0.5)
pyautogui.press('enter')  # Press Enter to select the option
sleep(2)
action.send_keys(Keys.ARROW_DOWN).perform()  # Navigate down
sleep(1)
action.send_keys(Keys.RETURN).perform()       # Press Enter
sleep(6)
pyautogui.click(x=100, y=100)

sleep(5)
driver.quit()