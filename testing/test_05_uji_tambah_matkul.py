from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_add_new_course(driver):
    marker_name = "Matkul Selenium Dasar"
    marker_sks = "2"
    marker_desc = "Data untuk pengujian otomatis selenium"

    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/courses"]').click()
    click_when_ready(driver, By.XPATH, '//a[@href="/courses/add"]').click()

    wait_for(driver, By.NAME, "course_name").send_keys(marker_name)
    wait_for(driver, By.NAME, "sks").send_keys(marker_sks)
    wait_for(driver, By.NAME, "description").send_keys(marker_desc)
    click_when_ready(driver, By.XPATH, "//button[text()='Tambah']").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/courses"))
    assert marker_name in driver.page_source
    take_screenshot(driver, "test_05_tambah_matkul")
