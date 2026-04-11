from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import BASE_URL, LOGIN_EMAIL, LOGIN_PASSWORD, take_screenshot, wait_for


def test_login_and_logout(driver):
    driver.get(f"{BASE_URL}/")

    wait_for(driver, By.NAME, "email").send_keys(LOGIN_EMAIL)
    wait_for(driver, By.NAME, "password").send_keys(LOGIN_PASSWORD)
    wait_for(driver, By.XPATH, '//button[@type="submit"]').click()

    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    assert "/dashboard" in driver.current_url
    take_screenshot(driver, "test_01_login_sukses")

    wait_for(driver, By.XPATH, "//a[@href='/logout']").click()
    WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
    assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")
    take_screenshot(driver, "test_01_logout_sukses")
