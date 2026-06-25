from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# Test Case: Positive Login
def test_positive_login(page: Page):
    login_page = LoginPage(page)
    
    # Alur test menjadi sangat bersih dan mirip bahasa manusia
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

from pages.login_page import LoginPage
from playwright.sync_api import expect

import pytest
from pages.login_page import LoginPage

# 🌟 Suntikkan variasi data uji (username, password, pesan error yang diharapkan)
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        # Data Kasus 1: Salah Password
        ("standard_user", "password_salah_asalan", "Epic sadface: Username and password do not match any user in this service"),
        # Data Kasus 2: Username Kosong
        ("", "secret_sauce", "Epic sadface: Username is required"),
        # Data Kasus 3: Password Kosong
        ("standard_user", "", "Epic sadface: Password is required"),
    ]
)
def test_negative_login_ddt(page, username, password, expected_error):
    login_page = LoginPage(page)
    
    # 1. Alur navigasi web
    login_page.navigate()
    
    # 2. Masukkan data dari list parameter di atas
    login_page.login(username, password)
    
    # 3. Ambil teks error dari elemen UI
    actual_error = login_page.get_error_message()
    
    # 4. Validasi kecocokan pesan error secara presisi
    assert actual_error == expected_error

# Test Case: Login dengan Dynamic Wait
def test_login_with_dynamic_wait(page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Jalankan aksi login standar
    login_page.login("standard_user", "secret_sauce")
    
    # Eksplisit menunggu komponen internal dashboard termuat sempurna
    login_page.wait_for_dashboard_loaded()
    
    # Assert akhir memastikan URL sudah sesuai
    assert page.url == "https://www.saucedemo.com/inventory.html"