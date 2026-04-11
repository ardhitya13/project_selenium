from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_navigasi_menu_joke(driver):
    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/joke"]').click()

    WebDriverWait(driver, 10).until(EC.url_contains("/joke"))
    heading = wait_for(driver, By.TAG_NAME, "h1").text.strip()
    assert "Joke of The Day" in heading
    take_screenshot(driver, "test_08_joke")
