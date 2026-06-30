import pytest
import logging
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# Inisialisasi Logger Instance khusus untuk UI Suite
logger = logging.getLogger(__name__)

# ==============================================================================
# UI SUITE: POSITIVE REGRESSION SKENARIO
# ==============================================================================
def test_positive_login(page: Page):
    logger.info("UI TEST START: Memulai skenario Positive Login SauceDemo.")
    login_page = LoginPage(page)
    
    logger.info("Membuka browser dan navigasi ke URL SauceDemo.")
    login_page.navigate()
    
    logger.info("Suntik kredensial data: standard_user.")
    login_page.login("standard_user", "secret_sauce")
    
    # Mempertahankan asersi sakti Playwright expect() dengan auto-wait
    logger.info("Validasi gerbang asersi: Memastikan URL beralih ke halaman Inventory Dashboard.")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    logger.info("UI POSITIVE TEST PASSED: Autentikasi sukses dan dashboard termuat sempurna!")


# ==============================================================================
# UI SUITE: DEFENSIVE EXTERNAL DATA-DRIVEN TESTING (DDT)
# ==============================================================================
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "password_salah_asalan", "Epic sadface: Username and password do not match any user in this service"),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
    ]
)
def test_negative_login_ddt(page: Page, username, password, expected_error):
    logger.warning(f"SECURITY CHECK: Menjalankan skenario Intrusion Defend untuk user: '{username}'")
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login(username, password)
    
    logger.info("Mengekstrak pesan eror visual dari elemen DOM UI via POM layer.")
    actual_error = login_page.get_error_message()
    
    # Asersi logika bisnis
    assert actual_error == expected_error
    logger.info(f"UI NEGATIVE TEST PASSED: Pesan eror [{expected_error}] tervalidasi secara presisi!")


# ==============================================================================
# UI SUITE: DYNAMIC EXPLICIT WAIT PERFORMANCE
# ==============================================================================
def test_login_with_dynamic_wait(page: Page):
    logger.info("UI WAIT OPTIMIZATION START: Memulai validasi Dynamic Wait Handling.")
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Meniru pola WaitForElement di C# .NET xUnit menggunakan explicit wait
    logger.info("Thread Block Preventer: Menunggu selektor '.inventory_list' muncul di DOM secara asinkron.")
    page.wait_for_selector(".inventory_list", timeout=5000)
    
    logger.info("UI TEST PASSED: Asinkronisasi render aman. Elemen visual terdeteksi tepat waktu.")