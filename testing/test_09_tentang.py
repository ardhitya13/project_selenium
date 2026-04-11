from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_navigasi_menu_tentang(driver):
    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/tentang"]').click()

    WebDriverWait(driver, 10).until(EC.url_contains("/tentang"))
    heading = wait_for(driver, By.TAG_NAME, "h1").text.strip()
    assert "Tentang SIM" in heading
    take_screenshot(driver, "test_09_tentang")
