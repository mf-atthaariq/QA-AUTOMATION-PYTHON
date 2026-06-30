import logging
from playwright.sync_api import Page, expect

# Inisialisasi Logger Instance khusus untuk Linear UI Suite
logger = logging.getLogger(__name__)

# --- SKENARIO POSITIF (INTEGRATED ENTERPRISE LOGGING) ---
def test_login_dan_add_to_cart_saucedemo(page: Page):
    logger.info("LINEAR UI START: Memulai skenario Positive Login & Add to Cart.")
    
    logger.info("Membuka browser dan memuat halaman login SauceDemo.")
    page.goto("https://www.saucedemo.com/")
    
    logger.info("Mengisi username: 'standard_user'.")
    page.fill("#user-name", "standard_user")
    
    logger.info("Mengisi secure password.")
    page.fill("#password", "secret_sauce")
    
    logger.info("Mengeksekusi klik pada tombol login.")
    page.click('[data-test="login-button"]')
    
    logger.info("Validasi transisi URL menuju halaman Inventory.")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    logger.info("Memilih produk 'Sauce Labs Backpack' dan memasukkannya ke keranjang belanja.")
    page.locator(".inventory_item", has_text="Sauce Labs Backpack").locator("button").click()
    
    badge_keranjang = page.locator(".shopping_cart_badge")
    logger.info("Memvalidasi jumlah counter badge pada ikon keranjang.")
    expect(badge_keranjang).to_have_text("1")
    
    logger.info("LINEAR UI POSITIVE TEST PASSED: Siklus login dan add to cart sukses penuh!")


# --- SKENARIO NEGATIF (INTEGRATED ENTERPRISE LOGGING) ---
def test_failed_login_saucedemo(page: Page):
    logger.warning("LINEAR UI SECURITY CHECK: Memulai skenario Negative Invalid Login.")
    
    logger.info("Navigasi ke landing page SauceDemo.")
    page.goto("https://www.saucedemo.com/")
    
    logger.info("Suntik data username salah: 'user_ngasal'.")
    page.fill("#user-name", "user_ngasal")
    
    logger.info("Suntik data password salah: 'password_salah'.")
    page.fill("#password", "password_salah")
    
    logger.info("Klik tombol submit login.")
    page.click('[data-test="login-button"]')
    
    # Selector untuk menangkap komponen error container di UI SauceDemo
    error_container = page.locator('[data-test="error"]')
    
    logger.info("Memvalidasi visibilitas dan teks pesan kesalahan pada layar.")
    expect(error_container).to_be_visible()
    expect(error_container).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    
    logger.info("LINEAR UI NEGATIVE TEST PASSED: Sistem berhasil menahan login ilegal dengan response pesan kesalahan yang valid!")