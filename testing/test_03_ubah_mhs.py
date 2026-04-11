from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot, wait_for


def test_update_student_info(driver):
    updated_name = "Mahasiswa Update"
    updated_address = "Batu Aji"

    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/mahasiswa"]').click()

    click_when_ready(
        driver,
        By.XPATH,
        "(//table[@class='table table-striped']//tr[position()=1]//a[text()='Ubah'])[1]",
    ).click()

    nama_input = wait_for(driver, By.NAME, "nama_lengkap")
    alamat_input = wait_for(driver, By.NAME, "alamat")
    nama_input.clear()
    nama_input.send_keys(updated_name)
    alamat_input.clear()
    alamat_input.send_keys(updated_address)

    click_when_ready(driver, By.XPATH, "//button[@type='submit']").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/mahasiswa"))
    assert updated_name in driver.page_source
    take_screenshot(driver, "test_03_ubah_mhs")
