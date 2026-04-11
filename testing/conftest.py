import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "http://127.0.0.1:9999"
LOGIN_EMAIL = "admin@if.local"
LOGIN_PASSWORD = "rahasia123"
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def click_when_ready(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )


def take_screenshot(driver, name):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(SCREENSHOT_DIR, f"{name}_{stamp}.png")
    driver.save_screenshot(file_path)
    return file_path


def login(driver):
    driver.get(f"{BASE_URL}/")
    wait_for(driver, By.NAME, "email").send_keys(LOGIN_EMAIL)
    wait_for(driver, By.NAME, "password").send_keys(LOGIN_PASSWORD)
    click_when_ready(driver, By.XPATH, '//button[@type="submit"]').click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))


@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
