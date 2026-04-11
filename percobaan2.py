from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com/")
time.sleep(3) #nunggu 3 detik

# Mencari dan mengklik link dengan isi a href /about
input_pencarian = driver.find_element(By.NAME, "q")
input_pencarian.send_keys("Tutorial Selenium")#supaya ga ngandelin modul aja
time.sleep(3) 

tombol_search = driver.find_element(By.XPATH, "//input[@name='btnK']")
tombol_search.click()
time.sleep(3) 

print("Pengujian googling selesai")

# Menutup browser setelah selesai
driver.quit()
