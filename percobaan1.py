from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.python.org/")
time.sleep(3)

# About
about_link = driver.find_element(By.XPATH, "//a[@href='/about/']")
about_link.click()
time.sleep(3)

# Balik ke homepage
driver.get("https://www.python.org/")
time.sleep(3)

# Downloads (ganti blogs)
downloads_link = driver.find_element(By.XPATH, "//a[@href='/downloads/']")
downloads_link.click()
time.sleep(3)

# Balik lagi
driver.get("https://www.python.org/")
time.sleep(3)

# Events
events_link = driver.find_element(By.XPATH, "//a[@href='/events/']")
events_link.click()
time.sleep(3)

print("Pengujian link web python.org selesai")
driver.quit()