from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_update_course(driver):
    base_name = "Matkul Selenium Dasar"
    updated_name = "Matkul Selenium Lanjutan"
    updated_sks = "3"
    updated_desc = "Data matakuliah sesudah update"

    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/courses"]').click()

    if base_name not in driver.page_source and updated_name not in driver.page_source:
        click_when_ready(driver, By.XPATH, '//a[@href="/courses/add"]').click()
        wait_for(driver, By.NAME, "course_name").send_keys(base_name)
        wait_for(driver, By.NAME, "sks").send_keys("2")
        wait_for(driver, By.NAME, "description").send_keys("Data awal")
        click_when_ready(driver, By.XPATH, "//button[text()='Tambah']").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/courses"))

    target_name = updated_name if updated_name in driver.page_source else base_name
    click_when_ready(
        driver,
        By.XPATH,
        f"//tr[td[contains(normalize-space(),'{target_name}')]]//a[text()='Ubah']",
    ).click()

    name_input = wait_for(driver, By.NAME, "course_name")
    sks_input = wait_for(driver, By.NAME, "sks")
    desc_input = wait_for(driver, By.NAME, "description")

    name_input.clear()
    name_input.send_keys(updated_name)
    sks_input.clear()
    sks_input.send_keys(updated_sks)
    desc_input.clear()
    desc_input.send_keys(updated_desc)

    click_when_ready(driver, By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/courses"))

    assert updated_name in driver.page_source
    take_screenshot(driver, "test_06_ubah_matkul")
