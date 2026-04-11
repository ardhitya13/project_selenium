from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_delete_course(driver):
    fallback_name = "Matkul Selenium Lanjutan"

    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/courses"]').click()

    if fallback_name not in driver.page_source:
        click_when_ready(driver, By.XPATH, '//a[@href="/courses/add"]').click()
        wait_for(driver, By.NAME, "course_name").send_keys(fallback_name)
        wait_for(driver, By.NAME, "sks").send_keys("2")
        wait_for(driver, By.NAME, "description").send_keys("Data untuk dihapus")
        click_when_ready(driver, By.XPATH, "//button[text()='Tambah']").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/courses"))

    click_when_ready(
        driver,
        By.XPATH,
        f"//tr[td[contains(normalize-space(),'{fallback_name}')]]//a[text()='Hapus']",
    ).click()

    Alert(driver).accept()
    WebDriverWait(driver, 10).until(EC.url_contains("/courses"))

    assert fallback_name not in driver.page_source
    take_screenshot(driver, "test_07_hapus_matkul")
