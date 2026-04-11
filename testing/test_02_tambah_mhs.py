from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_add_new_student(driver):
    marker_nim = "2305001"
    marker_nama = "Mahasiswa Selenium"
    marker_alamat = "Batam Center"

    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/mahasiswa"]').click()
    click_when_ready(driver, By.XPATH, '//a[@href="/mahasiswa/tambah"]').click()

    wait_for(driver, By.NAME, "nim").send_keys(marker_nim)
    wait_for(driver, By.NAME, "nama_lengkap").send_keys(marker_nama)
    wait_for(driver, By.NAME, "alamat").send_keys(marker_alamat)
    click_when_ready(driver, By.XPATH, "//button[text()='Tambah']").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/mahasiswa"))
    assert marker_nim in driver.page_source
    take_screenshot(driver, "test_02_tambah_mhs")
