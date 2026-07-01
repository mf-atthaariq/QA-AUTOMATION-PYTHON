import logging
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# Inisialisasi Logger Enterprise untuk BDD Suite
logger = logging.getLogger(__name__)

# 🌟 Mengikat (bind) skenario .feature secara otomatis ke fungsi Python di bawahnya
scenarios('../../features/user_login.feature')

@given('the user navigates to the SauceDemo login page')
def navigate_to_login(page: Page):
    logger.info("BDD [Given]: Menuju ke halaman login utama.")
    login_page = LoginPage(page)
    login_page.navigate()

@when(parsers.parse('the user enters username "{username}" and password "{password}"'))
def enter_credentials(page: Page, username, password):
    logger.info(f"BDD [When]: Mengisi kredensial username: '{username}' via POM layer.")
    login_page = LoginPage(page)
    # Gunakan method POM layer yang sudah lo buat sejak Week 3 le!
    login_page.page.fill("#user-name", username)
    login_page.page.fill("#password", password)

@when('clicks the login submit button')
def click_login(page: Page):
    logger.info("BDD [And]: Mengeksekusi ketukan tombol submit login.")
    login_page = LoginPage(page)
    login_page.page.click('[data-test="login-button"]')

@then('the user should be redirected to the inventory dashboard page')
def verify_dashboard(page: Page):
    logger.info("BDD [Then]: Memvalidasi asersi akhir status navigasi URL.")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    logger.info("BDD SCENARIO PASSED: Alur bisnis tervalidasi 100% ijo!")