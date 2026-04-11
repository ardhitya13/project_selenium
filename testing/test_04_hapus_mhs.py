from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import click_when_ready, login, take_screenshot


def test_delete_first_student(driver):
    login(driver)
    click_when_ready(driver, By.XPATH, '//a[@href="/mahasiswa"]').click()

    first_row_text = click_when_ready(
        driver, By.XPATH, "//table[@class='table table-striped']//tbody/tr[1]"
    ).text

    click_when_ready(
        driver,
        By.XPATH,
        "(//table[@class='table table-striped']//tr[position()=1]//a[text()='Hapus'])[1]",
    ).click()

    Alert(driver).accept()
    WebDriverWait(driver, 10).until(EC.url_contains("/mahasiswa"))

    assert first_row_text not in driver.page_source
    take_screenshot(driver, "test_04_hapus_mhs")
