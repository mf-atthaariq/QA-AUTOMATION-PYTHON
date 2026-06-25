class LoginPage:
    def __init__(self, page):
        self.page = page
        # Elemen Locator yang sudah ada
        self.username_input = "input#user-name"
        self.password_input = "input#password"
        self.login_button = "input#login-button"
        # 🌟 TAMBAHKAN LOCATOR INI (Menargetkan komponen error SauceDemo)
        self.error_message_container = "h3[data-test='error']"

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        if username:
            self.page.fill(self.username_input, username)
        if password:
            self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    # 🌟 TAMBAHKAN FUNGSI INI
    def get_error_message(self):
        # Mengambil teks yang muncul pada komponen error di web
        return self.page.locator(self.error_message_container).text_content()
    
    def wait_for_dashboard_loaded(self):
        # Menunggu hingga judul produk di dashboard benar-benar terlihat di layar
        self.page.wait_for_selector("span.title", state="visible", timeout=5000)