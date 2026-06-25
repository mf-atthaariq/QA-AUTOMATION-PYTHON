from playwright.sync_api import Page, expect

# --- SKENARIO POSITIF (YANG SUDAH KAMU BUAT) ---
def test_login_dan_add_to_cart_saucedemo(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click('[data-test="login-button"]')
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    page.locator(".inventory_item", has_text="Sauce Labs Backpack").locator("button").click()
    badge_keranjang = page.locator(".shopping_cart_badge")
    expect(badge_keranjang).to_have_text("1")
    print("\n[POS] Login & Add to cart sukses!")

# --- SKENARIO NEGATIF (BARU) ---
def test_failed_login_saucedemo(page: Page):
    # 1. Buka website
    page.goto("https://www.saucedemo.com/")
    
    # 2. Input Username yang SALAH
    page.fill("#user-name", "user_ngasal")
    
    # 3. Input Password yang SALAH
    page.fill("#password", "password_salah")
    
    # 4. Klik Tombol Login
    page.click('[data-test="login-button"]')
    
    # 5. Ambil selector untuk pesan error yang muncul
    # (Di Saucedemo, container error-nya memiliki atribut data-test="error")
    error_message = page.locator('[data-test="error"]')
    
    # 6. Assertion: Pastikan pesan error-nya muncul dan teksnya sesuai
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
    
    print("\n[NEG] Validasi error message sukses!")